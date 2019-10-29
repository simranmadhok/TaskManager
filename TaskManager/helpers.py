"""
        Helper functions for TaskManager file attachment attribute.
"""
import os
from datetime import date

def get_attachment_path(instance, filename):
        return os.path.join(f'Attachments/{instance.ckpt_date.date()}/{filename}')