period = int(input())

treated_patients = 0
untreated_patients = 0
doctor = 7

for counter in range(1, period + 1):
    patient = int(input())
    if counter % 3 == 0:
        if treated_patients < untreated_patients:
            doctor += 1
    if patient <= 7:
        treated_patients += patient
    else:
        untreated_patients += patient - doctor
        treated_patients += doctor

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
