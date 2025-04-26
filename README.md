# Skyrim Memory Reader

This Python script reads real-time in-game coordinates (X, Y) and the "Tamriel" state from the memory of the Skyrim Special Edition (SkyrimSE.exe) process. It outputs data in JSON format, including timestamps, facilitating easy data collection and analysis for game telemetry, mod development, or educational purposes.

## Prerequisites

- Python 3.x
- pymem library

Install dependencies using pip:

```bash
pip install pymem
```

## Usage

1. Run Skyrim Special Edition.
2. Execute the script in a terminal or command prompt:

```bash
python skyrim_memory_reader.py
```

## Output

The script outputs JSON-formatted data every second:

```json
{"timestamp": 1714135386, "x": -12432.34, "y": 12345.67, "tamriel": 1}
```

- **timestamp**: UNIX timestamp when data was recorded.
- **x**: Player's X-coordinate in the game world.
- **y**: Player's Y-coordinate in the game world.
- **tamriel**: Integer indicating if the player is within the Tamriel worldspace (specific meaning based on game context).

## Memory Offsets

- **Tamriel state (integer)**: `SkyrimSE.exe + 0x3196DE8`
- **Y-coordinate (float)**: `SkyrimSE.exe + 0x338A544`
- **X-coordinate (float)**: `SkyrimSE.exe + 0x338A540`

Ensure these offsets match your game version, as they may change with updates.
