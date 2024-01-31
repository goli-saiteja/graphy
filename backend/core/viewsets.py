
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import viewsets

from .models import Metrics, Departments
from .serializers import MetricsSerializer, DepartmentsSerializer 

@api_view(['GET'])
def insert(request):

    data = {
        "message": "test"
    }
    
    employee_metrics = [
        {
            "start_date": "2022-01-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 9,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "arts_and_design",
                    "new": 0,
                    "retained": 0,
                    "churned": 1
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-02-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 8,
                    "churned": 1
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-03-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 1,
                    "retained": 8,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-04-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 9,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-05-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 9,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-06-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 1,
                    "retained": 0,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 8,
                    "churned": 1
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-07-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 2,
                    "retained": 7,
                    "churned": 1
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 1,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-08-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 9,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 5,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-09-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 1,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 1,
                    "retained": 8,
                    "churned": 1
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 1
                }
            ]
        },
        {
            "start_date": "2022-10-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 1,
                    "retained": 9,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-11-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 2,
                    "retained": 10,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2022-12-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 11,
                    "churned": 1
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-01-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 11,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-02-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 2,
                    "retained": 11,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 1,
                    "retained": 4,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-03-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 7,
                    "retained": 12,
                    "churned": 1
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "education",
                    "new": 0,
                    "retained": 0,
                    "churned": 1
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 5,
                    "retained": 5,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-04-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 1,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 1,
                    "retained": 19,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 10,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-05-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 3,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 1,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 4,
                    "retained": 19,
                    "churned": 1
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 1,
                    "retained": 10,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-06-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "marketing",
                    "new": 1,
                    "retained": 0,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 1,
                    "retained": 23,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "arts_and_design",
                    "new": 1,
                    "retained": 0,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 11,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-07-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 4,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "marketing",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 24,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "arts_and_design",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 11,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-08-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 1,
                    "retained": 4,
                    "churned": 0
                },
                {
                    "functions": "accounting",
                    "new": 1,
                    "retained": 0,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "marketing",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 3,
                    "retained": 23,
                    "churned": 1
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "arts_and_design",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 2,
                    "retained": 11,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-09-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 5,
                    "churned": 0
                },
                {
                    "functions": "accounting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "marketing",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 5,
                    "retained": 26,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "arts_and_design",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 1,
                    "retained": 13,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-10-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 5,
                    "churned": 0
                },
                {
                    "functions": "accounting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "marketing",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 1,
                    "retained": 31,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "arts_and_design",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 14,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-11-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 0,
                    "retained": 5,
                    "churned": 0
                },
                {
                    "functions": "accounting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "marketing",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 0,
                    "retained": 32,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "arts_and_design",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 1,
                    "retained": 14,
                    "churned": 0
                }
            ]
        },
        {
            "start_date": "2023-12-01",
            "departments": [
                {
                    "functions": "others",
                    "new": 1,
                    "retained": 5,
                    "churned": 0
                },
                {
                    "functions": "accounting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "operations",
                    "new": 0,
                    "retained": 2,
                    "churned": 0
                },
                {
                    "functions": "marketing",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "engineering",
                    "new": 2,
                    "retained": 32,
                    "churned": 0
                },
                {
                    "functions": "consulting",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "arts_and_design",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "entrepreneurship",
                    "new": 0,
                    "retained": 1,
                    "churned": 0
                },
                {
                    "functions": "data_science",
                    "new": 0,
                    "retained": 15,
                    "churned": 0
                }
            ]
        }
    ]

    Metrics.objects.all().delete()
    Departments.objects.all().delete()
    for metric in employee_metrics:
        metricsInstance = Metrics()
        metricsInstance.start_date = metric["start_date"]
        metricsInstance.save()
        for department in metric["departments"]:
            Departments.objects.create(metric=metricsInstance, **department)
        print(metric["start_date"])
    return JsonResponse(data, safe=False)

class getMetrics(viewsets.ModelViewSet):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer

class getDepartments(viewsets.ModelViewSet):
    queryset = Departments.objects.all().order_by('metric__start_date')
    serializer_class = DepartmentsSerializer