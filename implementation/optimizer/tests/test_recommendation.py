import unittest

from macau_energy_optimizer import Recommendation, RecommendationMode


class RecommendationTest(unittest.TestCase):
    def test_default_mode_is_shadow(self) -> None:
        recommendation = Recommendation(
            recommendation_id="rec-001",
            tenant_id="tenant-demo",
            site_id="site-demo",
        )

        self.assertEqual(RecommendationMode.SHADOW, recommendation.mode)
        self.assertFalse(recommendation.requires_human_or_safety_path())


if __name__ == "__main__":
    unittest.main()
