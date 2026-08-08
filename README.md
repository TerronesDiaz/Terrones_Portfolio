# Francisco Terrones — Portfolio

Portafolio profesional bilingüe de Francisco Terrones, desarrollado con Astro 7 y Tailwind CSS 4. Incluye contenido en español e inglés, temas de color, CV descargables y una interfaz accesible y responsiva.

## Desarrollo local

Requiere Node.js 22 y npm.

```bash
npm ci
npm run dev
```

El sitio queda disponible en `http://localhost:4321`.

## Verificación

```bash
npm run check
npm run build
npm run audit
```

Para regenerar los CV se requiere Python con ReportLab:

```bash
npm run cv:generate
```

## Rutas

- `/`: versión en español.
- `/en/`: versión en inglés.
- `/cv/francisco-terrones-cv-es.pdf`: CV en español.
- `/cv/francisco-terrones-cv-en.pdf`: CV en inglés.

## Publicación

Los cambios enviados a `main` pasan por la verificación del contenedor y activan el despliegue automatizado definido en `.github/workflows/`.
