CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    capacity INTEGER NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

INSERT INTO rooms (name, capacity, available)
VALUES
('Conference Room A', 30, TRUE),
('Training Room B', 20, FALSE),
('Meeting Room C', 10, TRUE);

