static float probabilidadRespuesta;
    static int llamadasRespondidas = 0;
    static float probabilidadGenero;
    static float probabilidadVentaHombre;
    static float probabilidadVentaMujer;
    static float probabilidadCredito;
    static int creditosOtorgados = 0;
    static int creditoMujer = 0;
    static int creditoHombre = 0;
    static float comision = 0;
    static int repeticiones = 5000;
    static float sumaDesvEst = 0;

    public static void main(String[] args) {
        for (int i = 0; i < repeticiones; i++)
        {
            simular();
        }
        results();
    }

    static void simular()
    {
        probabilidadRespuesta = ThreadLocalRandom.current().nextFloat();
        if(probabilidadRespuesta <= 0.3)
        {
            llamadasRespondidas++;
            probabilidadGenero = ThreadLocalRandom.current().nextFloat();
            if(probabilidadGenero <= 0.20f)
            {
                probabilidadVentaHombre = ThreadLocalRandom.current().nextFloat();
                if(probabilidadVentaHombre <= 0.25f)
                {
                    probabilidadCredito = ThreadLocalRandom.current().nextFloat();
                    if(probabilidadCredito > 0.0f && probabilidadCredito <= 0.1f)
                    {
                        comision += 5000;
                        creditosOtorgados++;
                        creditoHombre++;
                        sumaDesvEst += Math.pow((((5000 / 5000) * 200) - 17),2);
                    }
                    else if(probabilidadCredito > 0.1f && probabilidadCredito <= 0.2f)
                    {
                        comision += 20000;
                        creditosOtorgados++;
                        creditoHombre++;
                        sumaDesvEst += Math.pow((((20000 / 5000) * 200) - 17),2);
                    }
                    else if(probabilidadCredito > 0.3f && probabilidadCredito <= 0.6f){
                        comision += 15000;
                        creditosOtorgados++;
                        creditoHombre++;
                        sumaDesvEst += Math.pow((((15000 / 5000) * 200) - 17),2);
                    }
                    else if(probabilidadCredito > 0.6f && probabilidadCredito < 1.0f){
                        comision += 10000;
                        creditosOtorgados++;
                        creditoHombre++;
                        sumaDesvEst += Math.pow((((10000 / 5000) * 200) - 17),2);
                    }
                }

            }
            else if(probabilidadGenero > 0.20f){
                probabilidadVentaMujer = ThreadLocalRandom.current().nextFloat();
                if(probabilidadVentaMujer <= 0.15f){
                    probabilidadCredito = ThreadLocalRandom.current().nextFloat();
                    if(probabilidadCredito > 0.0f && probabilidadCredito <= 0.6f){
                        comision += 5000;
                        creditosOtorgados++;
                        creditoMujer++;
                        sumaDesvEst += Math.pow((((5000 / 5000) * 200) - 17),2);
                    }
                    else if(probabilidadCredito > 0.6f && probabilidadCredito <= 0.9f){
                        comision += 10000;
                        creditosOtorgados++;
                        creditoMujer++;
                        sumaDesvEst += Math.pow((((10000 / 5000) * 200) - 17),2);
                    }
                    else if(probabilidadCredito > 0.9f && probabilidadCredito < 1.0f){
                        comision += 15000;
                        creditosOtorgados++;
                        creditoMujer++;
                        sumaDesvEst += Math.pow((((15000 / 5000) * 200) - 17),2);
                    }
                }
            }
        }
    }

    static void results(){
        float total = comision;
        comision = (comision / 5000)* 200;
        float desviacionEstandar = (float) Math.sqrt((sumaDesvEst / repeticiones));

        float intervaloConfianza1 =  (float) ((comision / repeticiones) + 1.65*(desviacionEstandar/Math.sqrt(5000)));
        float intervaloConfianza2 =  (float) ((comision / repeticiones) - 1.65*(desviacionEstandar/Math.sqrt(5000)));
        float media = total / creditosOtorgados;
        JOptionPane.showMessageDialog(null,"Total ventas: "+total+"\nComision: "+ comision +"\nPromedio llamada contestada y colocada: " + media +"\n"
                + "Promedio por llamada: "+ (comision / repeticiones) +"\nDesviacion Estandar: "+desviacionEstandar+"\n"
                        + "Intervalo de confianza: " + intervaloConfianza1+", "+intervaloConfianza2);
    }


}
