"""Tests for ticket priority calculation."""

import unittest

from campusflow.tickets import calculate_priority


class TestPriority(unittest.TestCase):
    """Boundary tests for the 4-rule priority engine."""

    def test_rule_1_critical(self):
        """high urgency + 10 or more users → critical."""
        # Boundary case: exactly 10
        self.assertEqual(calculate_priority("high", 10), "critical")
        # Above boundary
        self.assertEqual(calculate_priority("high", 12), "critical")

    def test_rule_2_high_by_urgency(self):
        """high urgency alone (fewer than 10 users) → high."""
        self.assertEqual(calculate_priority("high", 2), "high")
        # TODO: add one more case: high urgency + 9 users
        self.assertEqual(calculate_priority("high", 9), "high")

    def test_rule_2_high_by_user_count(self):
        """10 or more users alone (not high urgency) → high."""
        self.assertEqual(calculate_priority("low", 10), "high")
        # TODO: add one more case: medium urgency + 10 users
        self.assertEqual(calculate_priority("medium", 10), "high")

    def test_rule_3_medium_by_urgency(self):
        """medium urgency alone (fewer than 3 users) → medium."""
        self.assertEqual(calculate_priority("medium", 1), "medium")
        # TODO: add one more case: medium urgency + 2 users
        self.assertEqual(calculate_priority("medium", 2), "medium")

    def test_rule_3_medium_by_user_count(self):
        """3 or more users alone (low urgency) → medium."""
        self.assertEqual(calculate_priority("low", 3), "medium")
        # TODO: add one more case: low urgency + 4 users
        self.assertEqual(calculate_priority("low", 4), "medium")

    def test_rule_4_low(self):
        """low urgency + fewer than 3 users → low."""
        self.assertEqual(calculate_priority("low", 1), "low")
        # TODO: add one more case: low urgency + 2 users
        self.assertEqual(calculate_priority("low", 2), "low")


if __name__ == "__main__":
    unittest.main()
