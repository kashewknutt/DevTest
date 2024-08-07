from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.core.mail import send_mail
from django.conf import settings

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        email = request.POST['email']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)

        # Process the file
        df = pd.read_excel(fs.path(filename))

        # Ensure we are summing only numeric columns
        numeric_cols = df.select_dtypes(include='number').columns

        # Group by 'Cust State' and 'Cust Pin' and sum the numeric columns
        summary = df.groupby(['Cust State', 'Cust Pin'])[numeric_cols].sum().reset_index()

        # Convert summary DataFrame to string
        email_body = summary.to_string(index=False)

        # Send the summary report via email
        send_mail(
            subject='Python Assignment - Your Name',
            message=email_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        return render(request, 'upload/success.html', {'summary': summary.to_html()})
    return render(request, 'upload/upload.html')
