# Load flight data

Flights are now loaded from the **Flight** menu, not from a separate page.

- **Create**: choose an ArduPilot BIN file (or AcroWRX file). FCScore reads the file and shows its boot time, duration, logging rate and origin.
- Optionally add a Flight Coach JSON file to reuse its box and manoeuvre splits, then press **Continue to box setup**.
- BIN files should be logged at about 20 Hz. A warning appears below 18 Hz.
- If the file is already on the database a warning is shown. You can still analyse it but not upload it again.
- **Import** loads a BIN with a saved analysis (AJSON) file.

Next step: set the box at [the Box page](/fcscore/flight/new/box)

[Full instructions](https://pyflightcoach.github.io/FCScoreDocs/instructions/scoring/load_flight_data/)
