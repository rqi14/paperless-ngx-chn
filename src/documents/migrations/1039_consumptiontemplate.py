# Generated by Django 4.1.11 on 2023-09-16 18:04

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.db import migrations
from django.db import models
from django.db.models import Q


def add_consumptiontemplate_permissions(apps, schema_editor):
    # create permissions without waiting for post_migrate signal
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None

    add_permission = Permission.objects.get(codename="add_document")
    consumptiontemplate_permissions = Permission.objects.filter(
        codename__contains="consumptiontemplate",
    )

    for user in User.objects.filter(Q(user_permissions=add_permission)).distinct():
        user.user_permissions.add(*consumptiontemplate_permissions)

    for group in Group.objects.filter(Q(permissions=add_permission)).distinct():
        group.permissions.add(*consumptiontemplate_permissions)


def remove_consumptiontemplate_permissions(apps, schema_editor):
    consumptiontemplate_permissions = Permission.objects.filter(
        codename__contains="consumptiontemplate",
    )

    for user in User.objects.all():
        user.user_permissions.remove(*consumptiontemplate_permissions)

    for group in Group.objects.all():
        group.permissions.remove(*consumptiontemplate_permissions)


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("documents", "1038_sharelink"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConsumptionTemplate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=256, unique=True, verbose_name="name"),
                ),
                ("order", models.IntegerField(default=0, verbose_name="order")),
                (
                    "sources",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            (1, "Consume Folder"),
                            (2, "Api Upload"),
                            (3, "Mail Fetch"),
                        ],
                        default="1,2,3",
                        max_length=3,
                    ),
                ),
                (
                    "filter_path",
                    models.CharField(
                        blank=True,
                        help_text="Only consume documents with a path that matches this if specified. Wildcards specified as * are allowed. Case insensitive.",
                        max_length=256,
                        null=True,
                        verbose_name="filter path",
                    ),
                ),
                (
                    "filter_filename",
                    models.CharField(
                        blank=True,
                        help_text="Only consume documents which entirely match this filename if specified. Wildcards such as *.pdf or *invoice* are allowed. Case insensitive.",
                        max_length=256,
                        null=True,
                        verbose_name="filter filename",
                    ),
                ),
                (
                    "assign_change_groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="+",
                        to="auth.group",
                        verbose_name="grant change permissions to these groups",
                    ),
                ),
                (
                    "assign_change_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="grant change permissions to these users",
                    ),
                ),
                (
                    "assign_correspondent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="documents.correspondent",
                        verbose_name="assign this correspondent",
                    ),
                ),
                (
                    "assign_document_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="documents.documenttype",
                        verbose_name="assign this document type",
                    ),
                ),
                (
                    "assign_owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="assign this owner",
                    ),
                ),
                (
                    "assign_storage_path",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="documents.storagepath",
                        verbose_name="assign this storage path",
                    ),
                ),
                (
                    "assign_tags",
                    models.ManyToManyField(
                        blank=True,
                        to="documents.tag",
                        verbose_name="assign this tag",
                    ),
                ),
                (
                    "assign_view_groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="+",
                        to="auth.group",
                        verbose_name="grant view permissions to these groups",
                    ),
                ),
                (
                    "assign_view_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="grant view permissions to these users",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="owner",
                    ),
                ),
            ],
            options={
                "verbose_name": "consumption template",
                "verbose_name_plural": "consumption templates",
            },
        ),
        migrations.RunPython(
            add_consumptiontemplate_permissions,
            remove_consumptiontemplate_permissions,
        ),
    ]