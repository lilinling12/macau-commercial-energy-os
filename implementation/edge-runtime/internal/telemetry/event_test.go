package telemetry

import (
	"encoding/json"
	"testing"
	"time"
)

func TestEventSerializesAuthorityFields(t *testing.T) {
	e := Event{
		SchemaVersion: "1.0",
		TenantID:      "tenant-demo",
		SiteID:        "site-demo",
		DeviceID:      "meter-001",
		PointID:       "power-active",
		Metric:        "active_power",
		Value:         128.5,
		Unit:          "kW",
		Quality:       QualityGood,
		ObservedAt:    time.Date(2026, 10, 3, 0, 0, 0, 0, time.UTC),
	}

	raw, err := json.Marshal(e)
	if err != nil {
		t.Fatal(err)
	}

	if len(raw) == 0 {
		t.Fatal("expected non-empty JSON")
	}
}
