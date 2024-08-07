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

        # Process the file
        df = pd.read_excel(fs.path(filename))
        print(df.columns)  # Print columns for debugging

        # Prepare the summary report
        numeric_cols = df.select_dtypes(include='number').columns
        
        # Handle potential column conflicts
        try:
            summary = df.groupby(['Cust State', 'Cust Pin'], as_index=False)[numeric_cols].sum()
        except ValueError as e:
            # Handle specific error and return it in the response
            return render(request, 'upload/error.html', {'error': str(e)})

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
