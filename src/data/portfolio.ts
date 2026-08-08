export type Locale = 'es' | 'en';

export interface ExperienceEntry {
  role: string;
  company: string;
  location: string;
  period: string;
  current?: boolean;
  bullets: string[];
}

export interface ProjectEntry {
  title: string;
  description: string;
  image: string;
  imageAlt: string;
  href: string;
  linkLabel: string;
  tags: string[];
}

const shared = {
  email: 'f.terrones@outlook.com',
  linkedin: 'https://www.linkedin.com/in/francisco-javier-terrones-diaz',
  github: 'https://github.com/TerronesDiaz',
  whatsapp: 'https://wa.me/523121111440',
};

export const portfolioContent = {
  es: {
    locale: 'es' as Locale,
    path: '/',
    alternatePath: '/en/',
    cvPath: '/cv/francisco-terrones-cv-es.pdf',
    meta: {
      title: 'Francisco Terrones | Ingeniero de Software y SAP Business One',
      description:
        'Ingeniero de software en Colima especializado en soluciones a medida, SAP Business One, puntos de venta e integración de procesos empresariales.',
    },
    nav: {
      label: 'Navegación principal',
      menu: 'Abrir menú',
      close: 'Cerrar menú',
      links: [
        { href: '#inicio', label: 'Inicio' },
        { href: '#experiencia', label: 'Experiencia' },
        { href: '#proyectos', label: 'Proyectos' },
        { href: '#sobre-mi', label: 'Sobre mí' },
        { href: '#contacto', label: 'Contacto' },
      ],
      themeLabel: 'Tema visual',
      themes: { system: 'Sistema', light: 'Claro', dark: 'Oscuro' },
      languageLabel: 'Cambiar a inglés',
      languageShort: 'EN',
    },
    hero: {
      eyebrow: 'Ingeniería de software aplicada al negocio',
      title: 'Convierto procesos complejos en',
      highlight: 'soluciones que sí funcionan.',
      description:
        'Diseño productos a medida e integraciones con SAP Business One para mejorar ventas, operación, logística y toma de decisiones.',
      availability: 'Disponible para nuevos retos',
      primaryCta: 'Hablemos de tu proyecto',
      secondaryCta: 'Descargar CV en español',
      imageAlt: 'Retrato profesional de Francisco Javier Terrones Díaz',
      specialties: ['SAP Business One', 'POS y operaciones', '.NET · Svelte · SQL'],
      proof: [
        { value: '2024 - Hoy', label: 'Surtidora Ferretera' },
        { value: '2022 - Hoy', label: 'Desarrollo independiente' },
      ],
    },
    experienceSection: {
      eyebrow: 'Trayectoria',
      title: 'Experiencia que conecta software y operación',
      description:
        'Trabajo cerca de las personas que usan el sistema para convertir necesidades reales en herramientas claras, rápidas y sostenibles.',
      currentLabel: 'Actual',
    },
    experiences: [
      {
        role: 'Ingeniero de Software / Desarrollador SAP Business One',
        company: 'Surtidora de Ferretería y Materiales SFM',
        location: 'Colima, México',
        period: 'Julio 2024 - Hoy',
        current: true,
        bullets: [
          'Diseño e implementación de un punto de venta integral conectado con SAP Business One para ofertas, pedidos, ventas y facturación.',
          'Desarrollo de un portal interno que acompaña el flujo desde la venta y programación de documentos hasta la logística de embarque y los reportes administrativos.',
          'Optimización de consultas SQL y reestructuración de procesos para reducir cuellos de botella y mejorar el rendimiento del sistema.',
        ],
      },
      {
        role: 'Desarrollador de software independiente',
        company: 'Proyectos para pequeñas y medianas empresas',
        location: 'México',
        period: '2022 - Hoy',
        current: true,
        bullets: [
          'Creación de aplicaciones web, móviles y de escritorio enfocadas en resolver necesidades operativas concretas.',
          'Diseño de soluciones escalables con énfasis en facilidad de uso, automatización y mantenimiento.',
        ],
      },
      {
        role: 'Desarrollador Web',
        company: 'Puerto Inteligente Seguro',
        location: 'Manzanillo, México',
        period: 'Enero 2023 - Diciembre 2023',
        bullets: [
          'Desarrollo de formularios dinámicos para la captura estructurada de información operativa crítica del puerto.',
          'Creación de reportes a medida para identificar y analizar problemas de seguridad y apoyar la mejora de protocolos.',
        ],
      },
    ] satisfies ExperienceEntry[],
    projectsSection: {
      eyebrow: 'Trabajo seleccionado',
      title: 'Productos construidos para resolver',
      description:
        'Una muestra de plataformas empresariales, experiencias web e integraciones desarrolladas con objetivos concretos.',
    },
    projects: [
      {
        title: 'Terrones POS',
        description:
          'Sistema de punto de venta para pequeñas y medianas empresas, pensado para simplificar ventas, inventario y operación diaria.',
        image: '/media/img/TerronesPWA.webp',
        imageAlt: 'Interfaz del sistema de punto de venta Terrones POS',
        href: 'https://acortar.link/2G2rsJ',
        linkLabel: 'Ver demostración',
        tags: ['PWA', 'Operaciones', 'Inventario'],
      },
      {
        title: 'Portafolio profesional',
        description:
          'Sitio estático bilingüe creado con Astro, diseñado para cargar rápido y presentar experiencia y proyectos con claridad.',
        image: '/media/img/Portfolio.webp',
        imageAlt: 'Vista previa del portafolio profesional de Francisco Terrones',
        href: 'https://github.com/TerronesDiaz/Terrones_Portfolio',
        linkLabel: 'Explorar el código',
        tags: ['Astro', 'Tailwind CSS', 'Accesibilidad'],
      },
      {
        title: 'Asistente con inteligencia artificial',
        description:
          'Experiencia conversacional para responder preguntas, resolver dudas y acercar información de forma clara y eficiente.',
        image: '/media/img/ChatBot.webp',
        imageAlt: 'Interfaz de un asistente conversacional con inteligencia artificial',
        href: 'https://terronescolima.com',
        linkLabel: 'Conocer la solución',
        tags: ['IA', 'Automatización', 'Web'],
      },
    ] satisfies ProjectEntry[],
    about: {
      eyebrow: 'Sobre mí',
      title: 'Tecnología con contexto humano',
      paragraphs: [
        'Soy Francisco Javier Terrones Díaz, ingeniero de software de Colima. Me especializo en entender cómo trabaja una organización y traducir ese conocimiento en productos digitales confiables.',
        'He desarrollado soluciones web, móviles y de escritorio, integraciones empresariales y herramientas para operación diaria. Me interesa especialmente simplificar procesos, mejorar el rendimiento y dejar sistemas fáciles de mantener.',
      ],
      imageAlt: 'Francisco Terrones trabajando en una solución de software',
      educationLabel: 'Formación',
      education: 'Ingeniería de Software · Universidad de Colima · 2019 - 2023',
      skillsLabel: 'Especialidades',
      skills: ['JavaScript', 'C# / .NET', 'Svelte', 'SQL', 'SAP Business One', 'Frontend y backend'],
    },
    contact: {
      eyebrow: 'Contacto',
      title: '¿Tienes un proceso que el software podría mejorar?',
      description:
        'Cuéntame qué necesitas resolver. Podemos convertirlo en una herramienta útil, medible y preparada para crecer.',
      emailLabel: 'Enviar correo',
      linkedinLabel: 'Conectar en LinkedIn',
      whatsappLabel: 'Escribir por WhatsApp',
    },
    footer: 'Diseñado y desarrollado en Colima, México.',
    shared,
  },
  en: {
    locale: 'en' as Locale,
    path: '/en/',
    alternatePath: '/',
    cvPath: '/cv/francisco-terrones-cv-en.pdf',
    meta: {
      title: 'Francisco Terrones | Software Engineer and SAP Business One Developer',
      description:
        'Software engineer in Mexico specializing in custom solutions, SAP Business One, point-of-sale systems and business process integration.',
    },
    nav: {
      label: 'Main navigation',
      menu: 'Open menu',
      close: 'Close menu',
      links: [
        { href: '#home', label: 'Home' },
        { href: '#experience', label: 'Experience' },
        { href: '#projects', label: 'Projects' },
        { href: '#about', label: 'About' },
        { href: '#contact', label: 'Contact' },
      ],
      themeLabel: 'Visual theme',
      themes: { system: 'System', light: 'Light', dark: 'Dark' },
      languageLabel: 'Switch to Spanish',
      languageShort: 'ES',
    },
    hero: {
      eyebrow: 'Software engineering grounded in business',
      title: 'I turn complex processes into',
      highlight: 'solutions that work.',
      description:
        'I design custom products and SAP Business One integrations that improve sales, operations, logistics and decision-making.',
      availability: 'Open to new opportunities',
      primaryCta: 'Let’s discuss your project',
      secondaryCta: 'Download English résumé',
      imageAlt: 'Professional portrait of Francisco Javier Terrones Díaz',
      specialties: ['SAP Business One', 'POS and operations', '.NET · Svelte · SQL'],
      proof: [
        { value: '2024 - Present', label: 'Surtidora Ferretera' },
        { value: '2022 - Present', label: 'Independent development' },
      ],
    },
    experienceSection: {
      eyebrow: 'Career',
      title: 'Experience connecting software and operations',
      description:
        'I work closely with the people using each system to turn real needs into clear, fast and sustainable tools.',
      currentLabel: 'Current',
    },
    experiences: [
      {
        role: 'Software Engineer / SAP Business One Developer',
        company: 'Surtidora de Ferretería y Materiales SFM',
        location: 'Colima, Mexico',
        period: 'July 2024 - Present',
        current: true,
        bullets: [
          'Designed and implemented an end-to-end point-of-sale system connected to SAP Business One for quotations, orders, sales and invoicing.',
          'Built an internal portal covering sales, document scheduling, shipping logistics and administrative reporting workflows.',
          'Optimized SQL queries and restructured processes to reduce bottlenecks and improve overall system performance.',
        ],
      },
      {
        role: 'Independent Software Developer',
        company: 'Projects for small and medium-sized businesses',
        location: 'Mexico',
        period: '2022 - Present',
        current: true,
        bullets: [
          'Built web, mobile and desktop applications focused on concrete operational needs.',
          'Designed maintainable solutions centered on usability, automation and sustainable growth.',
        ],
      },
      {
        role: 'Web Developer',
        company: 'Puerto Inteligente Seguro',
        location: 'Manzanillo, Mexico',
        period: 'January 2023 - December 2023',
        bullets: [
          'Developed dynamic forms for structured collection of critical port operations information.',
          'Created custom reports to identify and analyze security issues and support protocol improvements.',
        ],
      },
    ] satisfies ExperienceEntry[],
    projectsSection: {
      eyebrow: 'Selected work',
      title: 'Products built to solve',
      description:
        'A selection of business platforms, web experiences and integrations developed around clear outcomes.',
    },
    projects: [
      {
        title: 'Terrones POS',
        description:
          'A point-of-sale system for small and medium-sized businesses, built to simplify sales, inventory and daily operations.',
        image: '/media/img/TerronesPWA.webp',
        imageAlt: 'Terrones POS point-of-sale interface',
        href: 'https://acortar.link/2G2rsJ',
        linkLabel: 'View demo',
        tags: ['PWA', 'Operations', 'Inventory'],
      },
      {
        title: 'Professional portfolio',
        description:
          'A bilingual static site built with Astro for fast loading and a clear presentation of experience and selected work.',
        image: '/media/img/Portfolio.webp',
        imageAlt: 'Preview of Francisco Terrones’s professional portfolio',
        href: 'https://github.com/TerronesDiaz/Terrones_Portfolio',
        linkLabel: 'Explore the code',
        tags: ['Astro', 'Tailwind CSS', 'Accessibility'],
      },
      {
        title: 'AI-powered assistant',
        description:
          'A conversational experience designed to answer questions, resolve doubts and make information easier to access.',
        image: '/media/img/ChatBot.webp',
        imageAlt: 'Artificial intelligence conversational assistant interface',
        href: 'https://terronescolima.com',
        linkLabel: 'View solution',
        tags: ['AI', 'Automation', 'Web'],
      },
    ] satisfies ProjectEntry[],
    about: {
      eyebrow: 'About me',
      title: 'Technology with human context',
      paragraphs: [
        'I’m Francisco Javier Terrones Díaz, a software engineer from Colima, Mexico. I specialize in understanding how an organization works and translating that knowledge into reliable digital products.',
        'I have built web, mobile and desktop solutions, business integrations and tools for daily operations. I care deeply about simplifying processes, improving performance and leaving systems that are easy to maintain.',
      ],
      imageAlt: 'Francisco Terrones working on a software solution',
      educationLabel: 'Education',
      education: 'B.S. in Software Engineering · University of Colima · 2019 - 2023',
      skillsLabel: 'Core skills',
      skills: ['JavaScript', 'C# / .NET', 'Svelte', 'SQL', 'SAP Business One', 'Frontend and backend'],
    },
    contact: {
      eyebrow: 'Contact',
      title: 'Is there a process your software could improve?',
      description:
        'Tell me what you need to solve. We can turn it into a useful, measurable tool that is ready to grow.',
      emailLabel: 'Send an email',
      linkedinLabel: 'Connect on LinkedIn',
      whatsappLabel: 'Message me on WhatsApp',
    },
    footer: 'Designed and built in Colima, Mexico.',
    shared,
  },
};

export type PortfolioContent = (typeof portfolioContent)[Locale];
