package br.com.gilmar;

import org.junit.Test;

import static org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class AvaliacaoTest {
    private int nota1;
    private int nota2;

    @Before
    public void setup(){
        aluno = new Avaliacao();
    }

    @Test(expected = ValoresInvalidosException.class)
    public void testCargaHoraria(){
        aluno.setNome("mateus");
        aluno.setNota1(4.5);
        aluno.setNota2(9.0);
        aluno.setFaltas(3);
        aluno.setCargaHoraria(-1);
        String avaliacao = aluno.avalia();
        String avaliacaoReferencia = "Aprovado";
        Assert.assertTrue(avaliacao == avaliacaoReferencia);
    }

    @Test(expected = ValoresInvalidosException.class)
    public void testFaltas(){
        aluno.setNome("mateus");
        aluno.setNota1(4.5);
        aluno.setNota2(9.0);
        aluno.setFaltas(3);
        aluno.setCargaHoraria(1);
        String avaliacao = aluno.avalia();
        /*String avaliacaoReferencia = "Aprovado";
        Assert.assertTrue(avaliacao == avaliacaoReferencia);*/
    }

    @Test(expected = ValoresInvalidosException.class)
    public void testNota1(){
        aluno.setNome("mateus");
        aluno.setNota1(-1.0);
        aluno.setNota2(9.0);
        aluno.setFaltas(3);
        aluno.setCargaHoraria(12);
        String avaliacao = aluno.avalia();
    }

    @Test(expected = ValoresInvalidosException.class)
    public void testNota2(){
        aluno.setNome("mateus");
        aluno.setNota1(4.3);
        aluno.setNota2(-1.0);
        aluno.setFaltas(3);
        aluno.setCargaHoraria(12);
        String avaliacao = aluno.avalia();
    }

    @Test
    public void testLimiteFaltas(){
        aluno.setNome("mateus");
        aluno.setNota1(4.3);
        aluno.setNota2(9.0);
        aluno.setFaltas(3);
        aluno.setCargaHoraria(8);
        String avaliacao = aluno.avalia();
        String esperado = "Reprovado por falta.";
        Assert.assertTrue(avaliacao == esperado);
    }

    @Test
    public void testNotaReprovado(){
        aluno.setNome("mateus");
        aluno.setNota1(4.3);
        aluno.setNota2(9.0);
        aluno.setFaltas(1);
        aluno.setCargaHoraria(12);
        String avaliacao = aluno.avalia();
        String esperado = "Reprovado por falta.";
        Assert.assertTrue(avaliacao == esperado);
    }

    @Test
    public void testProvaExtra(){
        aluno.setNome("mateus");
        aluno.setNota1(1.0);
        aluno.setNota2(10.0);
        aluno.setFaltas(1);
        aluno.setCargaHoraria(12);
        String avaliacao = aluno.avalia();
        String esperado = "Prova Extra.";
        Assert.assertTrue(avaliacao == esperado);
    }

    @Test
    public void testAprovado(){
        aluno.setNome("mateus");
        aluno.setNota1(6.0);
        aluno.setNota2(9.0);
        aluno.setFaltas(1);
        aluno.setCargaHoraria(12);
        String avaliacao = aluno.avalia();
        String esperado = "Aprovado.";
        Assert.assertTrue(avaliacao == esperado);
    }
}
