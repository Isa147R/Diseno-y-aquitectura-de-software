# Diseno-y-aquitectura-de-software
#https://docs.google.com/document/d/1VevGtO2aYT_tupjCKNFTlGMd9rnC1EDFM8hLDodLwG0/edit?usp=sharing

#Que es Solid?
#SOLID es un acrónimo que representa cinco principios de diseño de software que buscan crear sistemas más mantenibles, flexibles y escalables. Estos principios fueron presentados por Robert C. Martin y son ampliamente aceptados en la comunidad de desarrollo de software. Cada letra en "SOLID" representa un principio específico:

S - Principio de Responsabilidad Única (Single Responsibility Principle): Este principio establece que una clase o módulo debería tener una única responsabilidad. En otras palabras, una clase debe tener solo una razón para cambiar. Esto facilita el mantenimiento, ya que los cambios en una sola responsabilidad no afectarán otras partes del sistema.

O - Principio de Abierto/Cerrado (Open/Closed Principle): Este principio aboga por que las entidades de software (clases, módulos, etc.) deberían estar abiertas para la extensión pero cerradas para la modificación. En lugar de cambiar el código existente para agregar nuevas funcionalidades, se deben extender las clases o módulos existentes mediante herencia, interfaces u otros mecanismos, manteniendo así la estabilidad del código existente.

L - Principio de Sustitución de Liskov (Liskov Substitution Principle): Este principio se refiere a cómo las subclases deben poder sustituirse por sus clases base sin afectar el correcto funcionamiento del programa. En esencia, las subclases deben ser completamente intercambiables por sus clases base sin causar problemas en la coherencia del programa.

I - Principio de Segregación de Interfaces (Interface Segregation Principle): Según este principio, una interfaz no debería forzar a las clases a implementar métodos que no utilizan. En otras palabras, las interfaces deben ser específicas y contener solo los métodos necesarios para los clientes que las implementan. Esto evita la obligación de implementar métodos innecesarios y ayuda a evitar acoplamientos innecesarios entre componentes.

D - Principio de Inversión de Dependencia (Dependency Inversion Principle): Este principio sostiene que los módulos de alto nivel no deberían depender de los módulos de bajo nivel. En su lugar, ambos niveles deberían depender de abstracciones. Además, las abstracciones no deberían depender de los detalles; los detalles deberían depender de las abstracciones. Esto promueve la modularidad y la flexibilidad al reducir los acoplamientos directos entre componentes.

Estos principios SOLID se utilizan como guías para desarrollar software más modular, fácil de mantener y extensible. Al seguir estos principios, los desarrolladores pueden crear sistemas más robustos y adaptables a los cambios.
