"""Simulation and hardware integrations use explicit, vendor-neutral contracts."""

from .contracts import (
    CommandFeedback, CommandStatus, ConnectionStatus, RobotAdapter,
    RobotCapabilities, RobotCommand, RobotObservation,
)
from .spot import SpotAdapter, SpotAdapterConfig, SpotCredentials
from .simulation import SimulationAdapter, SimulationAdapterConfig
from .journal import CommandJournal

__all__ = [
    "CommandFeedback", "CommandStatus", "ConnectionStatus", "RobotAdapter",
    "RobotCapabilities", "RobotCommand", "RobotObservation", "SpotAdapter",
    "SpotAdapterConfig", "SpotCredentials",
    "SimulationAdapter", "SimulationAdapterConfig", "CommandJournal",
]
