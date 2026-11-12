from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

class Atendimento(ABC):
    
    def __init__(self, paciente: Paciente) -> None:
        self.paciente: Paciente = paciente
    
    @abstractmethod
    def duracao_minutos(self) -> int:
        pass
    
    def __str__ (self) -> str:
        return f"O antendimento {self.__class__.__name__}do Pacinete {self.paciente.nome} durou {self.duracao_minutos()} min"

class Consulta(Atendimento):
    def __init__(self, nome, cartao_sus, especialidade: str = " ", retorno: bool = False) -> None:
        super().__init__(nome, cartao_sus)
        self.especialidade = especialidade
        self.retorno = retorno


    def duracao_minutos(self) -> int:
        if self.retorno == True:
            return 15
        else:
            return 30

class Exame(Atendimento):
    def __init__(self, nome, cartao_sus, tipo: str = " ", jejum: bool = False) -> None:
        super().__init__(nome, cartao_sus)
        self.tipo = tipo
        self.jejum = jejum

    def duracao_minutos(self) -> int:
        if self.jejum == True:
            return 30
        else:
            return 20

class Vacinacao(Atendimento):
    def __init__(self, nome, cartao_sus, vacina: str = "", doses: int = 1) -> None:
        super().__init__(nome, cartao_sus)
        self.vacina = vacina
        self.doses = doses
    
    def duracao_minutos(self) -> int:
        return 10 * self.doses

class Agenda:

    def __init__(self, limite_minutos: int) -> None:
        self.limite_minutos = 240
        self._atendimentos: list[Atendimento] = []
    
    @property
    def atendimentos(self) -> str:
        return self._atendimentos
    
    @property
    def minutos_ocupados(self) -> int:
        return sum(atendimento.duracao_minutos() for atendimento in self._atendimentos)

    def agendar(self, atendimento: Atendimento) -> None:
        for agendado in self.__atendimentos:
            if agendado.paciente == atendimento.paciente:
                raise PacienteJaAgendadoError(f"O paciente {atendimento.paciente.nome} já possui atendimento agendado.")
            minutos_livres: int = (self._limite_minutos - self.minutos_ocupados)
            if atendimento.duracao_minutos() > minutos_livres:
                raise HorarioIndisponivelError(f"Tempo insuficiente na agenda. Minutos livres: {minutos_livres};necessários: {atendimento.duracao_minutos()}.")

        self.__atendimentos.append(atendimento)



            
