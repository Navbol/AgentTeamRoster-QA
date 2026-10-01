import { test, expect } from '@playwright/test';
import sqlite3 from 'sqlite3';

function consultarBD(sql: string, params: any[] = []): Promise<any[]> {
  return new Promise((resolve, reject) => {
    const db = new sqlite3.Database('nominas.db');
    db.all(sql, params, (err, rows) => {
      db.close();
      if (err) reject(err);
      else resolve(rows);
    });
  });
}

test.describe('Pruebas Automatizadas Data-Driven - Portal QA Fútbol', () => {

  test('Validar búsqueda por Selección consultando datos reales de la BD', async ({ page }) => {
    const filasBD = await consultarBD('SELECT DISTINCT seleccion FROM jugadores LIMIT 1');
    expect(filasBD.length).toBeGreaterThan(0);
    const seleccionPrueba = filasBD[0].seleccion;

    await page.goto('/');
    await page.locator('form[action="/buscar_seleccion"] input[name="seleccion"]').fill(seleccionPrueba);
    await page.locator('form[action="/buscar_seleccion"] button').click();

    await page.waitForLoadState('networkidle');
    await expect(page.locator('body')).toContainText(seleccionPrueba);
  });

  test('Agregar un nuevo jugador desde la web y verificar su guardado en la BD', async ({ page }) => {
    await page.goto('/');

    const nombrePrueba = 'Jugador QA ' + Date.now();

    // Llenar los campos del formulario
    await page.locator('form[action="/agregar_jugador"] input[name="seleccion"]').fill('Colombia');
    await page.locator('form[action="/agregar_jugador"] input[name="jugador"]').fill(nombrePrueba);
    await page.locator('form[action="/agregar_jugador"] input[name="posicion"]').fill('Delantero');
    await page.locator('form[action="/agregar_jugador"] input[name="edad"]').fill('25');
    await page.locator('form[action="/agregar_jugador"] input[name="equipo"]').fill('QA Club FC');

    // Hacer clic en el botón del formulario
    await page.locator('form[action="/agregar_jugador"] button').click();

    await page.waitForLoadState('networkidle');

    // Confirmar directamente la persistencia en la base de datos SQLite
    const jugadorEnBD = await consultarBD('SELECT * FROM jugadores WHERE jugador = ?', [nombrePrueba]);
    expect(jugadorEnBD.length).toBe(1);
    expect(jugadorEnBD[0].equipo).toBe('QA Club FC');
  });

});