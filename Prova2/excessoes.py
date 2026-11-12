class AgendaError(Exception):
    """Erros da classe Agenda"""

class HorarioIndisponivelError(AgendaError):
    """Horário Indisponível"""

class PacienteJaAgendadoError(AgendaError):
    """ Paciente já Agendado"""