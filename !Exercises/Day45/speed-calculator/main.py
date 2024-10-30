from enum import Enum
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QSpinBox, QPushButton
import sys


class MeasureSystem(Enum):
    METRIC = 'Metric (km)'
    IMPERIAL = 'Imperial (mi)'


class AvgSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setWindowTitle('Average Speed Calculator')

        # Create widgets
        distance_label = QLabel('Distance:')
        self.distance_edit = QSpinBox()
        self.distance_edit.setRange(1, 1000000000)
        self.measurement_system_combo = QComboBox()
        self.measurement_system_combo.addItems(
            [system.value for system in MeasureSystem])
        self.measurement_system_combo.setInsertPolicy(
            QComboBox.InsertPolicy.NoInsert)
        self.measurement_system_combo.setCurrentIndex(0)
        time_label = QLabel('Time (hours):')
        self.time_edit = QSpinBox()
        self.time_edit.setRange(1, 1000000000)
        calc_button = QPushButton('Calculate')
        calc_button.clicked.connect(self.calculate_speed)
        self.speed_label = QLabel('')

        # Add widgets to the layout
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_edit, 0, 1)
        grid.addWidget(self.measurement_system_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_edit, 1, 1)
        grid.addWidget(calc_button, 2, 1)
        grid.addWidget(self.speed_label, 3, 1, 1, 3)

        # Set the layout for the window
        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_edit.value())
        time = float(self.time_edit.value())
        speed = distance / time
        units = 'km/h' if self.measurement_system_combo.currentText() == MeasureSystem.METRIC.value else 'mph'
        self.speed_label.setText(
            f'Average speed: {speed:.4f} {units}')


app = QApplication(sys.argv)
speed_calculator = AvgSpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
