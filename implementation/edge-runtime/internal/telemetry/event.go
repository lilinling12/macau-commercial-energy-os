package telemetry

import "time"

type Quality string

const (
	QualityGood      Quality = "GOOD"
	QualityUncertain Quality = "UNCERTAIN"
	QualityBad       Quality = "BAD"
	QualityUnknown   Quality = "UNKNOWN"
)

type Event struct {
	SchemaVersion string    `json:"schemaVersion"`
	TenantID      string    `json:"tenantId"`
	SiteID        string    `json:"siteId"`
	DeviceID      string    `json:"deviceId"`
	PointID       string    `json:"pointId"`
	Metric        string    `json:"metric"`
	Value         any       `json:"value"`
	Unit          string    `json:"unit"`
	Quality       Quality   `json:"quality,omitempty"`
	ObservedAt    time.Time `json:"observedAt"`
}
