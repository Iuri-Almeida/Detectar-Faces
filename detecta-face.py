# Projeto Detecção de Face - Python, OpenCV e DLib
# Autor: Iuri Lopes Almeida
# Perfil GitHub: https://github.com/Iuri-Almeida
# Data: 30/05/2020
# Descrição: Esse programa foi escrito na linguagem Python e usou as
# 			 bibliotecas OpenCV e DLib como base. Ele faz a detecção
# 			 da face de uma pessoa e apresenta na tela desenhando um
# 			 retângulo ao redor da face. Além de mostrar a quantidade
# 			 de faces encontradas. Pode ser usado para vídeo (webcam)
# 			 ou para imagens (passando o caminho para a imagem).
# Forma de uso: python detecta-face.py


# Importações necessárias.
import cv2, dlib, imutils


# Função responsável por fazer a detecção da face em uma imagem.
# caminho_Imagem -> é o caminho para passar a imagem pro programa.
def detecta_Face_Foto(caminho_Imagem):

	print("[INFO] Iniciando o programa...")

	print("[INFO] Lendo a imagem...")

	# Função responsável por fazer a leitura da imagem.
	imagem = cv2.imread(caminho_Imagem)

	# A função get_frontal_face_detector() vai ser responsável por 'varrer'
	# toda a imagem entregue a ela e procurar por uma face.
	# Obs.: Se você já tiver usado o cascade para fazer detecção de faces,
	# 		essa função seria uma equivalente ao arquivo 'haarcascade', onde
	# 		contém as informações sobre o que é uma face.
	detector_Face = dlib.get_frontal_face_detector()

	print("[INFO] Aperte qualquer tecla para fechar.")

	# A função resize() é responsável por fazer o redimensionamento da
	# imagem.
	imagem = imutils.resize(imagem, width=600)

	# Aqui é onde a função get_frontal_face_detector() entra em ação. Ela
	# 'varre' todo a imagem e armazena em faces o 'id' de cada face e o
	# retângulo onde essa face foi detectada.
	# Obs.: O parâmetro 1 está relacionado ao quanto a imagem pode ser 
	# 		aumentada (zoom) para melhorar a detecção do rosto. Quanto
	# 		maior o valor melhor será a detecção, mas será preciso mais
	# 		poder de processamento. Em outras palavras, vai travar mais.
	faces = detector_Face(imagem, 1)

	# Para cada id e retângulo dentro das informações contidas em faces.
	# Obs.: A função enumerate() é responsável por fazer a identificação
	# 		de cada face encontrada com um id.
	for id_Face, retangulo in enumerate(faces):

		# Diferente do OpenCV, a DLib não retorna exatamente onde estão os
		# vértices do quadrado onde a face foi encontrada. Pra isso,
		# precisamos pegar as coordenadas desse retângulo.
		# x -> coordenada inicial em x.
		# y -> coordenada inicial em y.
		# l -> largura da imagem.
		# a -> altura da imagem.
		x = retangulo.left()
		y = retangulo.top()
		l = retangulo.right() - x
		a = retangulo.bottom() - y

		# Organizando os parâmetros para entender melhor.
		inicio_X = x
		inicio_Y = y
		fim_X = x + l
		fim_Y = y + a
		cor = (0, 0, 255)
		grossura_Linha = 2

		# Desenhe um retângulo usando as coordenadas de onde foi
		# encontrado uma face.
		cv2.rectangle(imagem, (inicio_X, inicio_Y), (fim_X, fim_Y), cor, grossura_Linha)

	# Organizando os parâmetros para entender melhor.
	texto = 'Faces: {}'.format(len(faces))
	coordenada_XY = (10, 30)
	fonte = cv2.FONT_ITALIC
	tamanho_Letra = 1
	cor = (0, 255, 0)
	grossura_Linha = 2

	# Escreva no frame.
	cv2.putText(imagem, texto, coordenada_XY, fonte, tamanho_Letra, cor, grossura_Linha)

	# Mostre na tela do computador.
	cv2.imshow('Detector de Faces em Imagem', imagem)

	# Função que será responsável por esperar e monitorar se alguma
	# tecla vai ser apertada.
	cv2.waitKey(0) & 0xFF

	print("[INFO] Terminando o programa...")

	# Função responsável por fechar todas as janelas abertas.
	cv2.destroyAllWindows()


# Função responsável por fazer a detecção da face em um vídeo.
def detecta_Face_Video():

	print("[INFO] Iniciando o programa...")

	print("[INFO] Abrindo o vídeo...")

	# Inicia a captura da imagem.
	# Obs.: Passando o parâmetro '0', o OpenCV entende que é para usar
	# 		a webcam. Caso queira usar um vídeo específico, basta passar
	# 		o caminho para o vídeo (Ex.: 'videos/exemplo.mp4').
	captura = cv2.VideoCapture(0)

	# A função get_frontal_face_detector() vai ser responsável por 'varrer'
	# toda a imagem entregue a ela e procurar por uma face.
	# Obs.: Se você já tiver usado o cascade para fazer detecção de faces,
	# 		essa função seria uma equivalente ao arquivo 'haarcascade', onde
	# 		contém as informações sobre o que é uma face.
	detector_Face = dlib.get_frontal_face_detector()

	print("[INFO] Aperte a tecla 'q' para fechar.")

	# Enquanto for verdade (loop infinito).
	# Obs.: Cada loop do while é um frame do vídeo.
	while True:

		# _ -> no Python podemos escolher não passar um parâmetro usando '_'.
		# frame -> é o frame (imagem) do vídeo que está sendo capturado.
		# A função read() é responsável por fazer a leitura de cada frame
		# do vídeo.
		_, frame = captura.read()

		# Se frame for vazio, ou seja, não tenha frame, pare o loop.
		if frame is None:
			break

		# A função resize() é responsável por fazer o redimensionamento do
		# frame.
		frame = imutils.resize(frame, width=500)

		# Aqui é onde a função get_frontal_face_detector() entra em ação. Ela
		# 'varre' todo o frame e armazena em faces o 'id' de cada face e o
		# retângulo onde essa face foi detectada.
		# Obs.: O parâmetro 1 está relacionado ao quanto o frame pode ser 
		# 		aumentado (zoom) para melhorar a detecção do rosto. Quanto
		# 		maior o valor melhor será a detecção, mas será preciso mais
		# 		poder de processamento.
		faces = detector_Face(frame, 1)

		# Para cada id e retângulo dentro das informações contidas em faces.
		# Obs.: A função enumerate() é responsável por fazer a identificação
		# 		de cada face encontrada com um id.
		for id_Face, retangulo in enumerate(faces):

			# Diferente do OpenCV, a DLib não retorna exatamente onde estão os
			# vértices do quadrado onde a face foi encontrada. Pra isso,
			# precisamos pegar as coordenadas desse retângulo.
			# x -> coordenada inicial em x.
			# y -> coordenada inicial em y.
			# l -> largura do frame.
			# a -> altura do frame.
			x = retangulo.left()
			y = retangulo.top()
			l = retangulo.right() - x
			a = retangulo.bottom() - y

			# Organizando os parâmetros para entender melhor.
			inicio_X = x
			inicio_Y = y
			fim_X = x + l
			fim_Y = y + a
			cor = (0, 0, 255)
			grossura_Linha = 2

			# Desenhe um retângulo usando as coordenadas de onde foi
			# encontrado uma face.
			cv2.rectangle(frame, (inicio_X, inicio_Y), (fim_X, fim_Y), cor, grossura_Linha)

		# Organizando os parâmetros para entender melhor.
		texto = 'Faces: {}'.format(len(faces))
		coordenada_XY = (10, 30)
		fonte = cv2.FONT_ITALIC
		tamanho_Letra = 1
		cor = (0, 255, 0)
		grossura_Linha = 2

		# Escreva no frame.
		cv2.putText(frame, texto, coordenada_XY, fonte, tamanho_Letra, cor, grossura_Linha)

		# Mostre na tela do computador.
		cv2.imshow('Detector de Faces em Video', frame)

		# Função que será responsável por esperar e monitorar se alguma
		# tecla vai ser apertada.
		key = cv2.waitKey(1) & 0xFF

		# Se a tecla apertada for o 'q', termine o loop.
		if key == ord('q'):
			break

	print("[INFO] Terminando o programa...")

	# Função responsável por fazer a liberação da captura.
	captura.release()

	# Função responsável por fechar todas as janelas abertas.
	cv2.destroyAllWindows()


# Função principal, onde serão chamadas as outras.
def main():

	# Chamando a função responsável por fazer a detecção da face em vídeo.
	# detecta_Face_Video()

	# Chamando a função responsável por fazer a detecção da face em imagem.
	# Passando a imagem para detectar.
	caminho_Imagem = 'imagens/80.jpg'

	detecta_Face_Foto(caminho_Imagem)


if __name__ == "__main__":
	main()