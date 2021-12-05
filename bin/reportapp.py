import httpx
import requests


def main():
    choice = input('[R]eport weather or [s]ee reports?')
    while choice:
        if choice.lower().strip() == 'r':
            report_event()
        elif choice.lower().strip() == 's':
            see_events()
        else:
            print(f"Don't know what to do with {choice}")
        choice = input('[R]eport weather or [s]ee reports?')


def report_event(is_reading_input=False):
    desc = input('What is happening now?')
    city = input("What city?")
    data = {
        "description": desc,
        "location": {
            "city": city,
        }
    }
    url = "http://127.0.0.1:8000/api/reports"
    response = requests.post(url=url, json=data)
    response.raise_for_status()
    result = response.json()
    print(f"Reported new event: {result.get('id')}")


def see_events():
    url = "http://127.0.0.1:8000/api/reports"
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()
    for r in data:
        print(f"{r.get('location').get('city')} has {r.get('description')}")

if __name__ == '__main__':
    main()
