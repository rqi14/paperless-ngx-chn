# Generated by Django 4.2.13 on 2024-06-28 17:52

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    replaces = [
        ("documents", "0004_auto_20160114_1844"),
        ("documents", "0005_auto_20160123_0313"),
        ("documents", "0006_auto_20160123_0430"),
        ("documents", "0007_auto_20160126_2114"),
        ("documents", "0008_document_file_type"),
        ("documents", "0009_auto_20160214_0040"),
        ("documents", "0010_log"),
        ("documents", "0011_auto_20160303_1929"),
    ]

    dependencies = [
        ("documents", "0003_sender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="sender",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="documents",
                to="documents.sender",
            ),
        ),
        migrations.AlterModelOptions(
            name="sender",
            options={"ordering": ("name",)},
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=128, unique=True)),
                ("slug", models.SlugField(blank=True)),
                (
                    "colour",
                    models.PositiveIntegerField(
                        choices=[
                            (1, "#a6cee3"),
                            (2, "#1f78b4"),
                            (3, "#b2df8a"),
                            (4, "#33a02c"),
                            (5, "#fb9a99"),
                            (6, "#e31a1c"),
                            (7, "#fdbf6f"),
                            (8, "#ff7f00"),
                            (9, "#cab2d6"),
                            (10, "#6a3d9a"),
                            (11, "#b15928"),
                            (12, "#000000"),
                            (13, "#cccccc"),
                        ],
                        default=1,
                    ),
                ),
                ("match", models.CharField(blank=True, max_length=256)),
                (
                    "matching_algorithm",
                    models.PositiveIntegerField(
                        choices=[
                            (1, "Any"),
                            (2, "All"),
                            (3, "Literal"),
                            (4, "Regular Expression"),
                        ],
                        default=1,
                        help_text='Which algorithm you want to use when matching text to the OCR\'d PDF.  Here, "any" looks for any occurrence of any word provided in the PDF, while "all" requires that every word provided appear in the PDF, albeit not in the order provided.  A "literal" match means that the text you enter must appear in the PDF exactly as you\'ve entered it, and "regular expression" uses a regex to match the PDF.  If you don\'t know what a regex is, you probably don\'t want this option.',
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="sender",
            name="slug",
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name="document",
            name="file_type",
            field=models.CharField(
                choices=[
                    ("pdf", "PDF"),
                    ("png", "PNG"),
                    ("jpg", "JPG"),
                    ("gif", "GIF"),
                    ("tiff", "TIFF"),
                ],
                default="pdf",
                editable=False,
                max_length=4,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="document",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                related_name="documents",
                to="documents.tag",
            ),
        ),
        migrations.CreateModel(
            name="Log",
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
                ("group", models.UUIDField(blank=True)),
                ("message", models.TextField()),
                (
                    "level",
                    models.PositiveIntegerField(
                        choices=[
                            (10, "Debugging"),
                            (20, "Informational"),
                            (30, "Warning"),
                            (40, "Error"),
                            (50, "Critical"),
                        ],
                        default=20,
                    ),
                ),
                (
                    "component",
                    models.PositiveIntegerField(
                        choices=[(1, "Consumer"), (2, "Mail Fetcher")],
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ("-modified",),
            },
        ),
        migrations.RenameModel(
            old_name="Sender",
            new_name="Correspondent",
        ),
        migrations.AlterModelOptions(
            name="document",
            options={"ordering": ("correspondent", "title")},
        ),
        migrations.RenameField(
            model_name="document",
            old_name="sender",
            new_name="correspondent",
        ),
    ]
