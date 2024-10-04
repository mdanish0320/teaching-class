import django
from django.conf import settings

# Setting up Django settings
if not settings.configured:
    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'rest_framework',
        ],
        REST_FRAMEWORK={
            'DEFAULT_PARSER_CLASSES': [
                'rest_framework.parsers.JSONParser',
            ],
            'DEFAULT_RENDERER_CLASSES': [
                'rest_framework.renderers.JSONRenderer',
            ]
        }
    )

# Initialize Django
django.setup()

from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    # CharField for names with constraints

    # IntegerField for age with constraints
    id = serializers.IntegerField(
        read_only=True,
        default=1
    )

    # EmailField for email address
    email = serializers.EmailField(
        max_length=254,  # Maximum length for email
        allow_blank=True
    )

    password = serializers.CharField(
        max_length=100,  # Maximum length for name
        min_length=4,    # Minimum length for name
        required=True,    # This field is required
        write_only=True,  # Cannot be blank
    )

    name = serializers.CharField(
        max_length=100,  # Maximum length for name
        min_length=1,    # Minimum length for name
        required=True,    # This field is required
        allow_blank=False,  # Cannot be blank
    )

    # IntegerField for age with constraints
    age = serializers.IntegerField(
        min_value=10,  # Minimum value for age
        max_value=80,  # Maximum value for age
        required=True,  # This field is required
    )

    # DateField for birth date
    birth_date = serializers.DateField(
        format='%Y-%m-%d',  # Date format
        input_formats=['%d-%m-%Y'],  # Accepted input formats
        required=False,  # This field is required
    )

    # ChoiceField for gender selection
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = serializers.ChoiceField(
        choices=GENDER_CHOICES,  # Fixed choices for gender
        default='O',             # Default value if not provided
    )

    # BooleanField for newsletter subscription
    newsletter_subscription = serializers.BooleanField(
        default=False,   # Default value if not provided
    )

json_data = {
    "id": 200,                      # read_only - user can only see the value but cannot create/update
    "email": "danish@gmail.com",    # equired
    "password": "1234",             # write_only - user can create the value but cannot read it
    "name": "danish",               # required
    "age": 30,                      # required
    "birth_date": "25-08-1994",     # input format is DD-MM-YYYY but python will receive the format as YYYY-MM-DD
    "gender": "M",
    "newsletter_subscription": False
}
serializer = CustomerSerializer(data=json_data)
if serializer.is_valid():
    print("valid data")
    print(serializer.validated_data) # read-only data will not show up i.e id
    print(serializer.validated_data['name'])
else:
    print(serializer.errors)

print(serializer.data) # write-only data will not show up i.e password