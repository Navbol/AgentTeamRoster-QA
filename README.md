# ⚽ QA Automation Portfolio: Data-Driven & E2E Testing

Proyecto de automatización de pruebas de punta a punta (E2E) y pruebas guiadas por datos (*Data-Driven Testing*) sobre una aplicación web construida en **Flask** y **SQLite**.

---

## 🛠️ Tecnologías y Herramientas

- **Backend & Web:** Python 3.12, Flask, Pandas, OpenPyXL
- **Base de Datos:** SQLite (`nominas.db`)
- **Framework de Pruebas:** Playwright (TypeScript), Node.js
- **Estrategia de Testing:** Data-Driven Testing (DDT), E2E Testing, Database Validation

---

## 🧪 Cobertura de Pruebas Automatizadas

1. **Consulta Data-Driven (BD vs UI):**
   - Extrae datos en tiempo real desde la base de datos `nominas.db` mediante SQL.
   - Realiza la búsqueda en la interfaz web de Flask y valida en el DOM la coincidencia de datos.

2. **Registro E2E + Validación en BD:**
   - Registra un nuevo jugador desde la interfaz web.
   - Valida directamente en SQLite la correcta persistencia del nuevo registro.

---

## 🚀 Cómo ejecutar el proyecto

### 1. Iniciar la aplicación Flask
```bash
python app.py