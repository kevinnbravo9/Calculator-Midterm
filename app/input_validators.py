"""Input validation for the calculator."""

from app.exceptions import ValidationError


def validate_number(value, max_value):
    """Validate that an input is numeric and within the allowed range."""
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValidationError("Input must be a number.") from exc

    if abs(number) > max_value:
        raise ValidationError(
            f"Input must be between {-max_value} and {max_value}."
        )

    return number