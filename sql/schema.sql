CREATE TABLE IF NOT EXISTS surgeries (
    surgery_id VARCHAR(20) PRIMARY KEY,
    patient_id VARCHAR(20) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    hospital VARCHAR(100) NOT NULL,
    room_id VARCHAR(20) NOT NULL,
    scheduled_date DATE NOT NULL,
    start_time TIME NOT NULL,
    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
    waiting_minutes INTEGER NOT NULL CHECK (waiting_minutes >= 0),
    emergency BOOLEAN NOT NULL,
    outcome VARCHAR(30) NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_surgeries_date ON surgeries(scheduled_date);
CREATE INDEX IF NOT EXISTS idx_surgeries_specialty ON surgeries(specialty);
CREATE INDEX IF NOT EXISTS idx_surgeries_hospital ON surgeries(hospital);
