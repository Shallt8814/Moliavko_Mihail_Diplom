from locust import HttpUser, task, between
class WebsiteTestUser(HttpUser):
    @task(1)
    def hello_world(self):
        self.client.get("http://localhost:5000")
    @task(2)
    def index(self):
        self.client.get("http://localhost:5000/index")