from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.core.mail import send_mail
from django.conf import settings

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        email = request.POST['email']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)

        df = pd.read_excel(fs.path(filename))
        print(df.columns) 

        numeric_cols = df.select_dtypes(include='number').columns
        

        try:
            summary = df.groupby(['Cust State', 'Cust Pin'], as_index=False)[numeric_cols].sum()
        except ValueError as e:
            return render(request, 'upload/error.html', {'error': str(e)})

        email_body = summary.to_string(index=False)

        send_mail(
            subject='Python Assignment',
            message=email_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        return render(request, 'upload/success.html', {'summary': summary.to_html()})
    return render(request, 'upload/upload.html')
