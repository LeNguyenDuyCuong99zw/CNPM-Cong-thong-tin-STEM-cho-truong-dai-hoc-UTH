from django.core.management.base import BaseCommand
from app.models import Report

class Command(BaseCommand):
    help = 'Generate daily reports'

    def handle(self, *args, **kwargs):
        report = Report()
        report.generate_report()
        self.stdout.write(self.style.SUCCESS('Successfully generated report for {}'.format(report.report_date)))