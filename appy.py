import streamlit as st
from PIL import Image 

st.title("CocinaFacil - Tu Asistente de Cocina Personalizado")
image = Image.open('Gatochef1.jpeg')
new_width = 200
new_height = 200
image_resized = image.resize((new_width, new_height))

# Mostrar la imagen con las nuevas dimensiones
st.image(image_resized, caption='Tu')
# Mensaje de Bienvenida y Saludo Personalizado
st.write("Bienvenido a CocinaFacil. Por favor, introduce tu nombre para comenzar:")
nombre = st.text_input("Nombre")

if nombre:
    st.write(f"¡Hola {nombre}! Soy ChefAI, tu asistente de cocina personal. ¿Estás listo para explorar nuevas recetas deliciosas?")

    # Opciones para el Usuario
    st.write("Por favor, responde las siguientes preguntas para recibir recomendaciones de recetas personalizadas:")

    plato = st.radio("¿Qué tipo de plato prefieres para tu comida principal?", ('Plato de carne', 'Plato vegetariano', 'Plato de pescado'))

    tiempo = st.radio("¿Cuánto tiempo tienes para cocinar?", ('Menos de 30 minutos', 'Entre 30 y 60 minutos', 'Más de 60 minutos'))

    cocina = st.radio("¿Qué tipo de cocina te gustaría explorar hoy?", ('Cocina mexicana', 'Cocina italiana', 'Cocina asiática'))

    # Recetas Seleccionadas según las Respuestas del Usuario
    st.subheader("Recetas Seleccionadas según tus Preferencias:")

    if plato == 'Plato de carne':
        if tiempo == 'Menos de 30 minutos':
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Tacos de Pollo Mexicano:")
                st.write("Descripción: Deliciosos tacos de pollo con un toque mexicano.")
                st.write("Ingredientes: Pollo desmenuzado, tortillas de maíz, cebolla, tomate, aguacate, cilantro, limón, salsa de tomate, especias mexicanas.")
                st.write("Instrucciones: Saltear el pollo con las especias, calentar las tortillas, y servir con los ingredientes frescos y salsa.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Espaguetis a la Boloñesa:")
                st.write("Descripción: Clásicos espaguetis con una deliciosa salsa de carne italiana.")
                st.write("Ingredientes: Espaguetis, carne molida, cebolla, ajo, zanahoria, salsa de tomate, vino tinto, aceite de oliva, especias italianas.")
                st.write("Instrucciones: Cocinar la carne con las verduras, agregar la salsa de tomate y el vino, cocinar a fuego lento, y servir sobre los espaguetis.")
            else: # Cocina asiática
                st.subheader("Receta de Pollo Teriyaki:")
                st.write("Descripción: Pollo marinado y glaseado con una deliciosa salsa teriyaki.")
                st.write("Ingredientes: Pechugas de pollo, salsa teriyaki, aceite de sésamo, jengibre, ajo, cebolla verde, arroz blanco.")
                st.write("Instrucciones: Marinar el pollo, dorarlo en la sartén con la salsa, y servir con arroz cocido.")

        elif tiempo == 'Entre 30 y 60 minutos':
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Enchiladas de Carne:")
                st.write("Descripción: Enchiladas rellenas de carne de res sazonada y cubiertas con salsa de enchilada.")
                st.write("Ingredientes: Carne de res molida, tortillas de maíz, salsa de enchilada, queso, cebolla, crema agria, cilantro.")
                st.write("Instrucciones: Cocinar la carne con especias, rellenar las tortillas, cubrir con salsa y queso, hornear y servir con acompañamientos.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Lasaña de Carne:")
                st.write("Descripción: Capas de pasta, carne y salsa de tomate, horneadas con queso derretido.")
                st.write("Ingredientes: Pasta para lasaña, carne molida, salsa de tomate, queso ricotta, mozzarella, parmesano, especias italianas.")
                st.write("Instrucciones: Cocinar la carne con la salsa, armar las capas con pasta y queso, hornear y servir caliente.")
            else: # Cocina asiática
                st.subheader("Receta de Stir Fry de Ternera y Verduras:")
                st.write("Descripción: Ternera salteada con una variedad de verduras frescas y salsa de soja.")
                st.write("Ingredientes: Ternera en tiras, verduras mixtas (pimientos, cebolla, brócoli), salsa de soja, jengibre, ajo, aceite de sésamo.")
                st.write("Instrucciones: Saltear la ternera y las verduras con la salsa de soja y las especias, servir caliente.")

        else: # Más de 60 minutos
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Barbacoa de Res:")
                st.write("Descripción: Carne de res cocida a fuego lento con una mezcla de especias y jugos.")
                st.write("Ingredientes: Carne de res (como la falda), mezcla de especias para barbacoa, cebolla, ajo, jugo de limón, consomé de res.")
                st.write("Instrucciones: Cocinar la carne lentamente con las especias y los jugos hasta que esté tierna y desmenuzable.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Osso Buco:")
                st.write("Descripción: Ternera estofada lentamente en vino y tomate, servida con gremolata.")
                st.write("Ingredientes: Rodajas de ternera con hueso, cebolla, zanahoria, apio, tomate, vino blanco, caldo de carne, perejil.")
                st.write("Instrucciones: Dorar la carne, cocinar las verduras, agregar el vino y el tomate, cocinar a fuego lento hasta que la carne esté tierna.")
            else: # Cocina asiática
                st.subheader("Receta de Curry de Pollo:")
                st.write("Descripción: Pollo y verduras cocidos en una salsa de curry aromática.")
                st.write("Ingredientes: Pechugas de pollo, verduras mixtas (pimientos, cebolla, zanahoria, brócoli), leche de coco, salsa de curry, jengibre, ajo.")
                st.write("Instrucciones: Saltear el pollo y las verduras, agregar la leche de coco y la salsa de curry, cocinar a fuego lento, servir con arroz.")
                
    elif plato == 'Plato vegetariano':
        if tiempo == 'Menos de 30 minutos':
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Ensalada Mexicana:")
                st.write("Descripción: Ensalada fresca con aguacate, maíz, frijoles y aderezo picante.")
                st.write("Ingredientes: Lechuga, aguacate, maíz, frijoles negros, tomate, cilantro, limón, aceite de oliva, chiles.")
                st.write("Instrucciones: Mezclar los ingredientes en un tazón, aderezar con limón y aceite de oliva, y servir frío.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Bruschetta de Tomate:")
                st.write("Descripción: Pan crujiente cubierto con tomates frescos, ajo y albahaca.")
                st.write("Ingredientes: Pan baguette, tomates, ajo, albahaca fresca, aceite de oliva, sal, pimienta.")
                st.write("Instrucciones: Tostar el pan, frotar con ajo, cubrir con tomates picados y albahaca, rociar con aceite de oliva y sazonar al gusto.")
            else: # Cocina asiática
                st.subheader("Receta de Salteado de Vegetales con Tofu:")
                st.write("Descripción: Vegetales frescos y tofu salteados en una salsa de soja y jengibre.")
                st.write("Ingredientes: Tofu firme, vegetales mixtos (pimientos, brócoli, zanahorias), salsa de soja, jengibre, ajo, aceite de sésamo.")
                st.write("Instrucciones: Saltear el tofu y los vegetales con la salsa de soja y las especias, servir caliente.")

        elif tiempo == 'Entre 30 y 60 minutos':
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Enchiladas Vegetarianas:")
                st.write("Descripción: Enchiladas rellenas de vegetales y cubiertas con salsa picante.")
                st.write("Ingredientes: Tortillas de maíz, vegetales mixtos (calabacín, maíz, pimientos), queso, salsa de enchilada, cilantro.")
                st.write("Instrucciones: Rellenar las tortillas con los vegetales, enrollar, cubrir con salsa y queso, hornear y servir con cilantro.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Risotto de Champiñones:")
                st.write("Descripción: Arroz cremoso cocido lentamente con champiñones y caldo de verduras.")
                st.write("Ingredientes: Arroz arborio, champiñones, caldo de verduras, cebolla, vino blanco, mantequilla, queso parmesano.")
                st.write("Instrucciones: Saltear la cebolla y los champiñones, agregar el arroz y el vino, cocinar lentamente agregando caldo, servir con queso rallado.")
            else: # Cocina asiática
                st.subheader("Receta de Curry de Verduras y Garbanzos:")
                st.write("Descripción: Verduras y garbanzos cocidos en una salsa de curry cremosa.")
                st.write("Ingredientes: Garbanzos cocidos, vegetales mixtos (coliflor, zanahorias, espinacas), leche de coco, salsa de curry, jengibre, ajo.")
                st.write("Instrucciones: Cocinar las verduras y los garbanzos en la salsa de curry, agregar la leche de coco, cocinar a fuego lento, servir con arroz.")

        else: # Más de 60 minutos
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Chile Relleno Vegetariano:")
                st.write("Descripción: Pimientos rellenos de arroz, frijoles y queso, cubiertos con salsa de tomate.")
                st.write("Ingredientes: Pimientos, arroz cocido, frijoles negros, queso, salsa de tomate, cilantro.")
                st.write("Instrucciones: Rellenar los pimientos con la mezcla de arroz, frijoles y queso, hornear con salsa de tomate, servir con cilantro.")

            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Lasagna de Verduras:")
                st.write("Descripción: Capas de verduras asadas y queso ricotta, horneadas con salsa de tomate y mozzarella.")
                st.write("Ingredientes: Berenjenas, calabacines, tomates, queso ricotta, salsa de tomate, mozzarella, albah                mo, parmesano, albahaca fresca.")
                st.write("Instrucciones: Asar las verduras, armar las capas con queso y salsa, hornear hasta que esté burbujeante y dorado.")
            else: # Cocina asiática
                st.subheader("Receta de Sopa de Miso con Tofu y Algas:")
                st.write("Descripción: Sopa de miso tradicional con tofu, algas y cebolla verde.")
                st.write("Ingredientes: Pasta de miso, tofu firme, algas nori, cebolla verde, caldo de vegetales.")
                st.write("Instrucciones: Disolver la pasta de miso en el caldo caliente, agregar el tofu y las algas, cocinar a fuego lento, servir con cebolla verde.")

    else: # Plato de pescado
        if tiempo == 'Menos de 30 minutos':
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Ceviche de Camarones:")
                st.write("Descripción: Camarones frescos marinados en jugo de limón y mezcla de vegetales.")
                st.write("Ingredientes: Camarones, jugo de limón, cebolla, tomate, cilantro, pepino, aguacate, chiles.")
                st.write("Instrucciones: Marinar los camarones en limón, mezclar con los vegetales picados, servir frío.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Pasta con Salmón y Espinacas:")
                st.write("Descripción: Pasta cocida con salmón fresco, espinacas y una salsa cremosa.")
                st.write("Ingredientes: Pasta, filete de salmón, espinacas, crema, queso parmesano, ajo, mantequilla.")
                st.write("Instrucciones: Cocinar la pasta, dorar el salmón y el ajo, agregar la crema y el queso, mezclar con las espinacas y la pasta.")
            else: # Cocina asiática
                st.subheader("Receta de Salmón Teriyaki:")
                st.write("Descripción: Filetes de salmón marinados y glaseados con salsa teriyaki.")
                st.write("Ingredientes: Filetes de salmón, salsa teriyaki, aceite de sésamo, jengibre, ajo, cebolla verde.")
                st.write("Instrucciones: Marinar el salmón en la salsa teriyaki, dorar en la sartén, rociar con más salsa y servir caliente.")

        elif tiempo == 'Entre 30 y 60 minutos':
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Pescado a la Veracruzana:")
                st.write("Descripción: Filetes de pescado en una salsa de tomate picante con aceitunas y alcaparras.")
                st.write("Ingredientes: Filetes de pescado blanco, salsa de tomate, cebolla, aceitunas, alcaparras, chiles, limón.")
                st.write("Instrucciones: Cocinar los filetes en la salsa con los condimentos, servir con arroz y limón.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Risotto de Mariscos:")
                st.write("Descripción: Arroz cremoso cocido con una variedad de mariscos frescos y caldo de pescado.")
                st.write("Ingredientes: Arroz arborio, camarones, calamares, mejillones, caldo de pescado, vino blanco, azafrán.")
                st.write("Instrucciones: Saltear los mariscos, agregar el arroz y el vino, cocinar lentamente agregando caldo, servir con azafrán.")
            else: # Cocina asiática
                st.subheader("Receta de Salmón al Vapor con Verduras:")
                st.write("Descripción: Filetes de salmón cocidos al vapor con una variedad de vegetales asiáticos.")
                st.write("Ingredientes: Filetes de salmón, bok choy, champiñones, zanahorias, jengibre, salsa de soja.")
                st.write("Instrucciones: Cocinar al vapor el salmón y las verduras con salsa de soja y jengibre, servir caliente.")

        else: # Más de 60 minutos
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Pescado Empapelado:")
                st.write("Descripción: Filetes de pescado sazonados y envueltos en papel de aluminio con verduras y limón.")
                st.write("Ingredientes: Filetes de pescado blanco, tomate, cebolla, pimiento, limón, cilantro, especias mexicanas.")
                st.write("Instrucciones: Sazonar el pescado, envolver con los vegetales y el limón, hornear y servir en el papel de aluminio.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Sopa de Pescado Italiana:")
                st.write("Descripción: Sopa espesa de pescado con tomate, ajo y hierbas frescas.")
                st.write("Ingredientes: Pescado blanco, tomate, cebolla, ajo, vino blanco, caldo de pescado, perejil.")
                st.write("Instrucciones: Cocinar el pescado y las verduras en el caldo con el vino, sazonar con hierbas y servir caliente.")
            else: # Cocina asiática
                st.subheader("Receta de Sushi de Salmón:")
                st.write("Descripción: Rollos de sushi rellenos de salmón fresco, aguacate y pepino.")
                st.write("Ingredientes: Arroz de sushi, filete de salmón, alga nori, aguacate, pepino, vinagre de arroz, wasabi, salsa de soja.")
                st.write("Instrucciones: Preparar el arroz, extender en las hojas de nori, añadir el salmón, aguacate y pepino, enrollar y cortar en porciones.")

     # Botón para Calificar la Experiencia
    st.subheader("¡Ayúdanos a mejorar tu experiencia! Por favor, califica CocinaFacil:")
    calificacion = st.slider("Califica de 1 a 5 estrellas", 1, 5)

    if calificacion:
        st.write(f"¡Gracias por tu calificación de {calificacion} estrellas!")

