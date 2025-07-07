import { useCallback } from 'react'
import { useDropzone } from 'react-dropzone';

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

    const files = acceptedFiles.map(file => (
        <li key={file.path}>
            {file.path} - {file.size} bytes
        </li>
    ));

    return (
        <div {...getRootProps()}>
            <input {...getInputProps()} />
            <Card className="w-full max-w-md">
                <CardContent className="flex flex-col items-center justify-center gap-3">
                    <CardTitle className="text-2xl">Adicione seus arquivos</CardTitle>
                    <Upload className="size-24 mb-2 text-muted-foreground" />

                    <p className="text-sm text-muted-foreground">
                        Suporte para arquivos SRT. <br /> Arraste e solte os arquivos aqui ou clique para selecionar.
                    </p>
                </CardContent>
            </Card>
            <ul>
                { files }
            </ul>
        </div>

    )
}


export { UploadSubtitles };
