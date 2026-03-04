from django.db import models


class BusinessSession(models.Model):
    idea = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.idea[:50]


class BusinessReport(models.Model):
    session = models.ForeignKey(BusinessSession, on_delete=models.CASCADE)

    market_analysis = models.TextField()
    financial_analysis = models.TextField()
    risk_analysis = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.session.id}"