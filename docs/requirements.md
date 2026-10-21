# CampusFlow Mastery — Requirements

## 1. Project Purpose

CampusFlow Mastery is a personal, from-scratch rebuild of CampusFlow
and CampusFlow-next.

The purpose is to build a complete IT helpdesk ticket management
application while developing the skills to implement, test, explain,
and maintain it independently.

## 2. Learning Principles

- Implement features in small, understandable steps.
- Write and run tests as features are developed.
- Use feature branches and pull requests.
- Obtain human review before merging changes.
- Understand and explain every implementation decision.
- Preserve existing work and avoid unreviewed changes to main.

## 3. Scope

The project will combine the requirements of both CampusFlow and
CampusFlow-next into one coherent application.

The final feature inventory and detailed acceptance criteria will
be documented in this file before the corresponding features are
considered complete.

## 4. Ticket Statuses

The application must use exactly these four statuses:

- `open`
- `in_progress`
- `resolved`
- `closed`

No additional ticket statuses may be introduced.

## 5. Completion Standard

A feature is not complete merely because its code runs.

It must have appropriate tests, documented behaviour, understandable
implementation decisions, and human review through a pull request.

## 6. Ticket Data and Validation

Every ticket must contain these fields:

- `id`: A unique ticket identifier beginning with `T` followed by at
  least three digits, such as `T001`.
- `title`: A required, non-empty title.
- `category`: One of `Network`, `Hardware`, `Software`, or `Other`.
- `urgency`: One of `high`, `medium`, or `low`.
- `affected_users`: A non-negative integer.
- `priority`: Calculated by the priority rules in Section 7.
- `status`: One of the four statuses defined in Section 4.
- `assigned_to`: The assignee's name, or an empty value when unassigned.

Invalid input must be rejected clearly. Validation must not silently
change invalid input into a valid value.

Boolean values must not be accepted as integers for numeric fields.
Ticket identifiers must be unique.

## 7. Priority Calculation

Priority must be calculated using these rules, in this exact order:

1. If urgency is `high` and `affected_users` is at least 10,
   priority is `critical`.
2. Otherwise, if urgency is `high` or `affected_users` is at least 10,
   priority is `high`.
3. Otherwise, if urgency is `medium` or `affected_users` is at least 3,
   priority is `medium`.
4. Otherwise, priority is `low`.

The priority engine must return the correct result for every valid
combination of urgency and affected users.

Tests must cover every rule, boundary values, and invalid inputs.
Priority must be recalculated when relevant ticket information changes.

## 8. Assignment and Ticket Workflow

New tickets must begin with status `open`.

A ticket may be assigned to a named person. Assignment must reject
an empty or whitespace-only assignee name.

A ticket must be assigned before it can move to `in_progress`.
An attempt to start work on an unassigned ticket must be rejected
without changing the ticket.

The application must use only these four statuses:

- `open`
- `in_progress`
- `resolved`
- `closed`

Workflow changes must validate the requested status and the current
ticket state before making changes.

A resolved ticket must be reopened to `open` before it can be
modified. Reopening must not introduce a separate status.

Invalid workflow changes must produce a clear error and preserve
the ticket's existing data.

Tests must cover valid transitions, invalid transitions, assignment
requirements, and attempts to modify resolved tickets.

## 9. Search, Sorting, and Work Queue

The application must support searching tickets by:

- Title
- Category
- Status
- Priority

When multiple search filters are supplied, all supplied filters
must match the same ticket. Filters must be combined using AND logic.

The application must support sorting tickets by priority and by
numeric ticket identifier. Ticket identifiers must be sorted by
their numeric portions, so `T002` comes before `T010`.

The unresolved-ticket queue must contain only tickets whose status
is `open` or `in_progress`.

The queue must sort tickets by priority, from highest to lowest,
and then by numeric ticket identifier to provide a consistent order
when priorities are equal.

Searching, sorting, and displaying the queue must not modify stored
tickets.

Tests must cover each search field, combined filters, sorting order,
empty results, and exclusion of `resolved` and `closed` tickets
from the unresolved queue.

## 9. Search, Sorting, and Work Queue

The application must support searching tickets by title, category,
status, and priority.

When multiple search filters are supplied, all supplied filters
must match the same ticket. Filters must use AND logic.

The application must support sorting by priority and numeric ticket
identifier. IDs must be sorted by their numeric portions, so `T002`
comes before `T010`.

The unresolved-ticket queue must contain only tickets with status
`open` or `in_progress`.

The queue must sort by priority from highest to lowest, followed by
numeric ticket identifier when priorities are equal.

Search, sorting, and queue display must not modify ticket data.

Tests must cover individual and combined filters, sorting, empty
results, and exclusion of resolved and closed tickets.

## 10. JSON Persistence and Data Integrity

The application must save tickets and their follow-up notes to JSON
and load them again when the application starts.

Saved data must preserve ticket fields, statuses, assignments,
priorities, and note identifiers and contents.

When loading data, the application must validate the structure and
required fields. Invalid records and duplicate ticket identifiers
must not be silently accepted.

If loading fails, existing in-memory records must remain unchanged.

Saving must report failures clearly. Where practical, writes must
use a temporary file and atomic replacement to reduce the risk of
partially written data.

A failed save must not be reported as successful.

Tests must cover saving, loading, persistence across restarts,
invalid JSON, invalid records, duplicate IDs, and storage failures.

## 11. Follow-Up Notes

Tickets must support multiple follow-up notes.

Each note must contain:

- `note_id`: A unique, sequential identifier such as `N001`, `N002`,
  and `N003`.
- `author`: A required, non-empty author name.
- `message`: A message containing between 5 and 300 characters.

New notes must receive new identifiers. Existing note identifiers
must never be reused or changed when another note is added.

The application must preserve existing notes when adding new notes
or saving and loading tickets.

A resolved ticket must be reopened to `open` before it is modified.
Adding a note must follow the ticket workflow rules.

Invalid notes must be rejected without silently changing existing
notes or ticket data.

Tests must cover note validation, sequential identifiers, multiple
notes, persistence, and invalid operations.

## 12. Reports and Calculations

The application must provide reports containing:

- Total number of tickets.
- Counts for each of the four statuses.
- Counts by priority.
- Counts by category.
- Total number of unresolved tickets.
- Number of resolved tickets and resolution percentage.
- Total number of affected users.

Unresolved tickets are tickets with status `open` or `in_progress`.

The resolution percentage must be calculated from the number of
resolved tickets divided by the total number of tickets, multiplied
by 100.

When there are no tickets, the resolution percentage must be `0`;
the application must not crash because of division by zero.

Report calculations must use the current ticket data and must not
modify it.

Tests must cover empty data, mixed statuses, priority and category
counts, affected-user totals, and percentage calculations.

## 13. Command-Line Interface

The application must provide a clear command-line menu for accessing
its supported features.

The menu must make available the implemented ticket operations,
including creation, assignment, workflow changes, searching,
sorting, unresolved queue display, notes, reports, and persistence.

Invalid menu choices and invalid user input must produce clear
messages and allow the user to continue where possible.

The interface must not crash or corrupt ticket data when a user
enters invalid input.

The interface must separate user interaction from the underlying
ticket and business logic wherever practical.

Tests must cover menu input handling and important user workflows.

## 14. Engineering Understanding-Check

The application must include an engineering understanding-check
containing six multiple-choice questions.

Each question must provide four options labelled A, B, C, and D.

The program must validate answers, reject invalid choices, and allow
the user to try again when an answer is invalid.

The final score must be displayed out of six.

The understanding-check must assess actual project behaviour,
including validation, workflow rules, persistence, searching or
reporting, and error handling.

It must also provide at least two prompts for explaining design
decisions or discussing the implementation with a human reviewer.

The question bank, answer checking, scoring, and user interaction
should be separated where practical.

Tests must cover correct answers, incorrect answers, invalid input,
score calculation, and explanation prompts.

## 15. Demo Data and Project Documentation

The project must provide clearly identified demo data that allows
the main features to be demonstrated without requiring manual entry
of every ticket.

Demo data must follow the same validation and workflow rules as
ordinary ticket data.

The README and supporting documentation must explain how to set up,
run, test, and demonstrate the application.

Documentation must describe the project structure, supported
features, ticket statuses, priority rules, and important design
decisions.

Demo data must not overwrite a user's existing data without
explicit confirmation.

## 16. Acceptance Criteria and Definition of Done

The project is complete only when:

- All required ticket fields and validation rules are implemented.
- Priority calculation follows Section 7 exactly.
- Assignment and workflow rules are enforced.
- Search, sorting, and the unresolved queue behave as specified.
- Tickets and notes persist correctly through JSON storage.
- Reports return correct results, including for empty data.
- The command-line interface supports the required operations.
- The six-question understanding-check works correctly.
- Automated tests cover normal cases, boundary cases, and failures.
- Setup and usage instructions are documented.
- The user can explain the main implementation decisions and
  demonstrate the application.
- Changes have been reviewed through pull requests before merging.

A passing test suite alone does not establish completion. Behaviour
must also match these requirements, and important design decisions
must be understandable and explainable.

## 17. Development and Review Rules

Features must be implemented in small, testable increments.

Each feature must include appropriate automated tests.

Changes must be developed on a suitable feature branch and submitted
through a pull request for human review.

Existing work must be inspected before changes are made. Unrelated
changes must not be included in a feature's pull request.

A feature must not be described as complete until its behaviour has
been checked against the relevant requirements and its tests pass.
