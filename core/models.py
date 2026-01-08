from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Task(models.Model):
    """
    Represents a decision/task item in the urgency matrix.
    Scoring Login: Timeframe + Cost of Inaction + Reward = Priority Score.
    """

    # Link the task to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    
    title = models.CharField(max_length=200, help_text="The task you want to evaluate (e.g., 'Learn Guitar')")

    # Metric 1: Timeframe (Urgency)
    # Scale: 1 (Can wait) -> 10 (Immediate)
    
    urgency_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Timeframe (Urgency)",
        help_text="Scale 1-10: How soon must this be done?"
    )
    
    # Metric 2: Cost of Inaction (Risk)
    # Scale: 1 (No risk) -> 10 (High consequence)
    risk_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Cost of Inaction",
        help_text="Scale 1-10: What is the penalty if you DON'T do this?"
    )
    
    # Metric 3: Reward (ROI)
    # Scale: 1 (Low impact) -> 10 (Life changing)
    reward_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Reward / ROI",
        help_text="Scale 1-10: How beneficial is the outcome?"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at'] # Default sort: newest first
        
    def __str__(self):
        return self.title
    
    @property
    def total_score(self):
        """
        Calculates the raw sum of the 3 metrics.
        Used to determine the size of the block in the pyramid.
        """
        return self.urgency_score + self.risk_score + self.reward_score