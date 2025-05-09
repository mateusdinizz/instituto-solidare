from django.db import models
from usuario.models import InformacoesPessoais
# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cursos_imagens/', blank=True, null=True)
    documento = models.FileField(upload_to='documentos_cursos/', blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    alunos = models.ManyToManyField(InformacoesPessoais, blank=True)

    def _str_(self):
        return f'{self.nome} - {self.curso.nome}'
    
class Frequencia(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(InformacoesPessoais, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=True)

    class Meta:
        unique_together = ('turma', 'aluno', 'data')

    def __str__(self):
        return f"{self.aluno.user.username} - {self.data} - {'Presente' if self.presente else 'Faltou'}"