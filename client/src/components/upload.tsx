import { useCallback } from 'react'
import { useDropzone } from 'react-dropzone';
import { File, Files } from 'lucide-react';

import { Button } from "@/components/ui/button";

import {
    Card,
    CardAction,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"

import { Upload } from 'lucide-react';

function UploadSubtitles() {
    const { acceptedFiles, getRootProps, getInputProps } = useDropzone();

    if (acceptedFiles.length === 0) {
        const files =
            acceptedFiles.map(file => (
                <Card key={file.path} className='p-6 w-full'>
                    <div className='flex flex-col items-start content-center w-full gap-2'>
                        <p className="text-left text-sm">{file.path}</p>
                        <p>{Math.floor(file.size / 1024)} KB</p>
                    </div>
                </Card>
            ));
    } else { 
        const files = 


     }

    return (
        <div {...getRootProps()}>
            <div className="flex flex-row justify-around items-top gap-3 p-4">
                <div className="rounded-md h-full grow">
                    <div className="flex items-center justify-center gap-4 opacity-50">
                        <p className="text-lg text-center">Arquivos adicionados</p>
                        <File />
                    </div>
                    <div className='flex flex-col gap-2 p-4 overflow-y-auto h-full'>
                        {
                            <div>
                                <Button>
                                    Confirm
                                </Button>
                            </div>
                        }
                    </div>
                </div>

                <div className="border-l w-0.5 flex-none" >
                    {/* Vertical Separator */}
                </div>

                <input {...getInputProps()} />
                <Card className="w-full max-w-md hover:scale-105 transition-normal ease-in-out">
                    <CardContent className="flex flex-col items-center justify-center gap-3">
                        <CardTitle className="text-2xl">Adicione seus arquivos</CardTitle>
                        <Upload className="size-24 mb-2 text-muted-foreground" />

                        <p className="text-sm text-muted-foreground">
                            Suporte para arquivos SRT. <br /> Arraste e solte os arquivos aqui ou clique para selecionar.
                        </p>
                    </CardContent>
                </Card>

                <div className="flex-none">
                </div>
            </div>
        </div>
    )
}


export { UploadSubtitles };
