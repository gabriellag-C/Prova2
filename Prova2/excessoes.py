class AgendaError(Exception):
    pass

class HorarioIndisponivelError(AgendaError):
    """Horario Indisponivel"""

class PacienteJaAgendadoError(AgendaError):
    """ Paciente já Agendado"""