# Preguntas técnicas

Responda las siguientes preguntas en un archivo de rebajas llamado Answers.md.

1. ¿Cuánto tiempo dedicó a la prueba de codificación de backend?

   4 Horas

2. ¿Qué agregarías a tu solución si tuvieras más tiempo?

   Un sistema de roles de usuario y terminar diseño responsive

3. ¿Cuales fueron los motivos de tu elección de arquitectura para este tipo de aplicación ?

   Se utilizó el marco de trabajo Django debido a que facilita mucho la implementación de la base de datos, el diseño de los controladores y sus validaciones necesarias, además de que incluye un sitio de administrador bastante completo de forma automática.

   Se utilizó el marco de trabajo Vue3 / Nuxt3 para la aplicación web porque estas herramientas permiten tener una estructura de código muy modular, flexible y que permite escalar la aplicación de forma muy rápida y segura.

4. ¿Cómo se pueden gestionar los casos posteriores a la medianoche para que se muestren el mismo día y no el siguiente?

   Para poder gestionar estos casos es necesario crear una validación en el componente visual de sesiones en donde se valide los campos de fecha y aplicar el rango permitido para un día.

5. ¿Cuánto tiempo dedicó a la prueba de codificación frontend? ¿Cuáles fueron tus mayores dificultades?

   Dediqué a cabo 8 horas de desarrollo en las que el mayor desafío fue definir la estructura óptima de componentes, entidades y servicios, para que el sitio sea escalable y rápido.

6. ¿Cómo localizaría un problema de rendimiento en producción? ¿Alguna vez has tenido que hacer esto?

   Para poder localizar un problema en un entorno de producción, además de la definición de pruebas unitarias, debo escuchar los comentarios de mis usuarios, encontrar los problemas que tengan y poder llevar a cabo las actualizaciones pertinentes.

7. ¿Cuál fue la característica más útil que se agregó a la última versión del lenguaje elegido? Incluya un fragmento de código que muestre cómo lo ha utilizado.

   Para la aplicación web usé las opciones de programación funcional dadas por Javascript lo que permite tener un código más lógico, entendible y mantenible, además de trasformar datos entro tipo de forma rápida.

   ```typescript
   onBeforeMount(async () => {
     const response = await studentService.all();

     // Se transformar los datos del servidor en data usable por el campo select de estudiantes
     students.value = response.map((item: Student) => ({
       value: item.id,
       label: `${item.firstName} ${item.lastName}`,
     }));
   });
   ```

8. ¿Que elementos de seguridad hubiera incluido en su API?

   Un sistema de roles, permisos y perfiles más completos
