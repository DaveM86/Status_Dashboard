# Status Dashboard
Dashboard application displaying the state of deployable server sets and their core elements.<n/>
---
Database schema
---
```mermaid
erDiagram
    DSS ||--|{ Build: contains
    DSS ||--o{ Message: contains
    User ||--|{ Message: contains
    Message ||--|{ Reply: contains
    User ||--|{ Reply: contains
    DSS ||--|{ Fault: contains
    User ||--|{ Fault: contain
    User ||--|{ AdhockTask: contains
    DSS ||--o{ ScheduledTask: "may contain"
    DSS ||--o{ AdhockTask: "may contain"
    ScheduledTask ||--|{ TodaysTasks: contains
    User ||--|{ TodaysTasks: contains
    DSS{
        Text db_num PK "The database Number"
        Text title
        Text serviceable
        Text comments
    }
    User{
        Text id PK "Unique User ID"
        Text first_name
        Text last_name     
    }
    Build {
        Text id PK "Unique Build Ref ID"
        Text DSS_database FK "DSS Table Database Number"
        Numeric date_started
        Text current_stage
        Numeric date_completed
        Text comments
    }
    Message {
        Text id PK "Unique Message ID"
        Text created_by FK "User Table ID"
        Text DSS_database FK "DSS Table Database Number"
        Text content
        Numeric date_created
    }
    Reply {
        Numeric id PK "Unique Reply ID"
        Text initial_message_id FK "Unique Message ID"
        Text created_by FK "User Table ID"
        Text content
        Numeric date_created       
    }
    Fault {
        Text fault_ref PK "Unique Fault ID"
        Text raised_by FK "User Table ID"
        Text DSS_database FK "DSS Table Database Number"
        Numeric date_created
        Text status
        Text description
    }
    ScheduledTask {
        Numeric id PK "Unique Fault ID"
        Text raised_by FK "User Table ID"
        Text description
        Numeric date_due
        Text status
        Text notes
        Numeric date_created
    }
    AdhockTask {
        Text id PK "Unique Fault ID"
        Text raised_by FK "User Table ID"
        Text completed_by FK "User Table ID"
        Text description
        Numeric date_due
        Text status
        Text notes
        Numeric date_time_completed
        Numeric date_created
    }
    TodaysTasks {
        Numeric id PK "Todays Task ID"
        Numeric sheduled_task FK "Schedulaed Task ID"
        Text completed_by FK "User Table ID"
        Numeric date_time_completed
    }
```
---
Database Schema Tasking
```mermaid
erDiagram
    User ||--|{ AdhockTask: contains
    DSS ||--o{ ScheduledTask: "may contain"
    DSS ||--o{ AdhockTask: "may contain"
    ScheduledTask ||--|{ TodaysTasks: contains
    User ||--|{ TodaysTasks: contains
    DSS{
        Text db_num PK "The database Number"
        Text title
        Text serviceable
        Text comments
    }
    User{
        Text id PK "Unique User ID"
        Text first_name
        Text last_name     
    }
    ScheduledTask {
        Numeric id PK "Unique Fault ID"
        Text raised_by FK "User Table ID"
        Text description
        Numeric date_due
        Text status
        Text notes
        Numeric date_created
    }
    AdhockTask {
        Text id PK "Unique Fault ID"
        Text raised_by FK "User Table ID"
        Text completed_by FK "User Table ID"
        Text description
        Numeric date_due
        Text status
        Text notes
        Numeric date_time_completed
        Numeric date_created
    }
    TodaysTasks {
        Numeric id PK "Todays Task ID"
        Numeric sheduled_task FK "Schedulaed Task ID"
        Text completed_by FK "User Table ID"
        Numeric date_time_completed
    }
```
---
Database Schema Messaging
```mermaid
erDiagram

    DSS ||--o{ Message: contains
    User ||--|{ Message: contains
    Message ||--|{ Reply: contains
    User ||--|{ Reply: contains
    DSS{
        Text db_num PK "The database Number"
        Text title
        Text serviceable
        Text comments
    }
    User{
        Text id PK "Unique User ID"
        Text first_name
        Text last_name     
    }
    Message {
        Text id PK "Unique Message ID"
        Text created_by FK "User Table ID"
        Text DSS_database FK "DSS Table Database Number"
        Text content
        Numeric date_created
    }
    Reply {
        Numeric id PK "Unique Reply ID"
        Text initial_message_id FK "Unique Message ID"
        Text created_by FK "User Table ID"
        Text content
        Numeric date_created       
    }
```
