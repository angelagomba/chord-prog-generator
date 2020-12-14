from enum import Enum

class LSMethod(Enum):
  SIMPLE_HC = 'simple hill climbing'
  STEEPEST_ASCENT_HC = 'steepest ascent hill climbing'
  STOCHASTIC_HC = 'stochastic hill climbing'