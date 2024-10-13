```plantuml
@startuml Dispositivi
class Dispositivo {
  - marca: str
  - modello: str
  - prezzo: float
  - disponibile: bool
  + get_marca() -> str
  + set_marca(marca: str) -> None
  + get_modello() -> str
  + set_modello(modello: str) -> None
  + get_prezzo() -> float
  + set_prezzo(prezzo: float) -> None
  + is_disponibile() -> bool
  + set_disponibile(disponibile: bool) -> None
  + vendi() -> None
  + rifornisci() -> None
  + descrizione() -> str
  + {static} numero_dispositivi: int
  + {static} conta_dispositivi() -> int
  + {static} calcola_sconto(prezzo: float, percentuale: float) -> float
}

class Smartphone {
  - memoria: int
  + get_memoria() -> int
  + set_memoria(memoria: int) -> None
  + descrizione() -> str
}

class Laptop {
  - ram: int
  + get_ram() -> int
  + set_ram(ram: int) -> None
  + descrizione() -> str
}

class Tablet {
  - dimensione_schermo: float
  + get_dimensione_schermo() -> float
  + set_dimensione_schermo(dimensione_schermo: float) -> None
  + descrizione() -> str
}

class Inventario {
  - dispositivi: List[Dispositivo]
  + aggiungi_dispositivo(dispositivo: Dispositivo) -> None
  + stampa_inventario() -> None
  + cerca_per_prezzo(prezzo: float) -> List[Dispositivo]
  + cerca_disponibili() -> List[Dispositivo]
}

Dispositivo <|-- Smartphone
Dispositivo <|-- Laptop
Dispositivo <|-- Tablet
Inventario --> Dispositivo
@enduml