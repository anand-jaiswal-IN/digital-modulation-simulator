# Digital Modulation Simulator

A Python-based simulator for fundamental digital modulation techniques: Amplitude Shift Keying (ASK), Frequency Shift Keying (FSK), and Phase Shift Keying (PSK). This educational tool allows users to input binary data and visualize the corresponding modulated waveforms, facilitating a deeper understanding of digital communication concepts.

## Features

- **Amplitude Shift Keying (ASK):** Modulates binary data by varying the amplitude of the carrier signal.
- **Frequency Shift Keying (FSK):** Represents binary data through changes in the frequency of the carrier signal.
- **Phase Shift Keying (PSK):** Encodes binary data by altering the phase of the carrier signal.
- **Visualization:** Generates time-domain plots for each modulation scheme using Matplotlib.
- **Modular Design:** Structured codebase with separate modules for signal generation and modulation techniques.([Flocode][1])

## Project Structure

```bash
.
├── main.py
├── modulated_signal.png
├── modulations.py
├── signal_generation.py
├── pyproject.toml
├── uv.lock
├── README.md
```

- `main.py`: Entry point of the application; handles user input and invokes modulation functions.
- `modulations.py`: Contains implementations of ASK, FSK, and PSK modulation techniques.
- `signal_generation.py`: Provides functions for generating carrier signals and handling binary data.
- `modulated_signal.png`: Sample output image showcasing the modulated waveforms.
- `pyproject.toml`: Project metadata and dependencies managed by `uv`.
- `uv.lock`: Lock file ensuring consistent dependency versions.([Real Python][2], [Astral Docs][3])

## Prerequisites

- **Python Version:** Ensure Python 3.11 or higher is installed.
- **uv:** A fast Python package and project manager.([Astral Docs][4], [GitHub][5])

To install `uv`, follow the official installation guide: [uv Installation](https://docs.astral.sh/uv/install/)([Astral Docs][6])

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/anand-jaiswal-IN/digital-modulation-simulator.git
   cd digital-modulation-simulator
   ```

2. **Synchronize Dependencies:**

   ```bash
   uv sync
   ```

This command will create a virtual environment and install all necessary dependencies as specified in `pyproject.toml`.

## Usage

Run the simulator using the following command:

```bash
uv run main.py
```

Upon execution, the program will prompt you to enter a binary string (e.g., `1011001`). It will then generate and display the corresponding ASK, FSK, and PSK modulated waveforms. Additionally, the combined plot will be saved as `modulated_signal.png` in the project directory.

## Customization

- **Modulation Parameters:** You can adjust parameters such as carrier frequency, amplitude, and bit duration within the respective functions in `modulations.py` and `signal_generation.py` to observe different modulation behaviors.

- **Input Validation:** Enhance the `main.py` script to include input validation for binary strings to ensure robustness.

## Acknowledgments

- Developed as part of the Communication Engineering curriculum.
- Utilizes the `uv` project manager for efficient dependency and environment management.
- Inspired by educational resources on digital modulation techniques.([Real Python][2], [Astral Docs][3])

[1]: https://flocode.substack.com/p/044-python-environments-again-uv?utm_source=chatgpt.com "#044 | uv: A Guide to Python Package Management"
[2]: https://realpython.com/python-uv/?utm_source=chatgpt.com "Managing Python Projects With uv: An All-in-One Solution"
[3]: https://docs.astral.sh/uv/guides/projects/?utm_source=chatgpt.com "Working on projects | uv - Astral Docs"
[4]: https://docs.astral.sh/uv/concepts/projects/init/?utm_source=chatgpt.com "Creating projects | uv - Astral Docs"

[5]: https://github.com/gdamjan/uv-getting-started?utm_source=chatgpt.com "An example \"getting started\" python project based on `uv` - GitHub"
[6]: https://docs.astral.sh/uv/concepts/projects/config/?utm_source=chatgpt.com "Configuring projects | uv - Astral Docs"
[7]: https://github.com/astral-sh/uv-docker-example/blob/main/pyproject.toml?utm_source=chatgpt.com "pyproject.toml - astral-sh/uv-docker-example - GitHub"
