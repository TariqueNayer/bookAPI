from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.
class Book(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False,
	)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=500)
	description = models.TextField()

	def __str__(self):
		return self.title


class Order_Status(models.TextChoices):
		# Value stored in database  | Human-readable name
		PENDING = "WT", "Pending"
		PAID = "PD", "Paid"
		CANCELLED = "CN", "Cancelled"


class Order(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False,
	)

	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	book = models.ForeignKey(
		Book, on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)

	book_history = models.CharField(max_length=500, editable=False, help_text="Stores UUID | Title | [Status]")

	

	status = models.CharField(
		max_length=2,
		choices=Order_Status.choices,
		default=Order_Status.PENDING,
	)

	@property
	def book_display_info(self):
		if self.book:
			return f"{self.book.id} | {self.book.title}"
		else:
			return f"{self.book_history} [Discontinued]"

	def save(self, *args, **kwargs):

		if self._state.adding and self.book:
			self.book_history = f"{self.book.id} | {self.book.title}"

		super().save(*args, **kwargs)

	