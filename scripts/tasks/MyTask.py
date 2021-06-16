from cumulusci.tasks.salesforce import BaseSalesforceApiTask

class MyTask(BaseSalesforceApiTask):
    def _run_task(self):
        print('This is my task.')