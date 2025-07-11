import { Header } from "@/components/header";
import { UploadSubtitles } from "@/components/upload";
import { Footer } from "@/components/footer";
import { Page } from "@/components/page";

import { SiGithub, SiGmail } from "@icons-pack/react-simple-icons";

import { File } from "lucide-react";

const links = [
    {
        text: "GitHub",
        url: "https://github.com/ravivendraminidealmeida",
        icon: <SiGithub />
    },
    {
        text: "Email",
        url: "https://github.com/ravivendraminidealmeida",
        icon: <SiGmail />
    }
];

function Hero() {
    return (
        <Page header={<Header />} footer={<Footer links={links} />}>
            <div className="w-full py-8 px-4 flex flex-col gap-3">
                <p className="text-5xl font-bold text-center">
                    Traduza legendas de forma
                    simples e eficiente
                </p>

                <UploadSubtitles />
            </div>
        </Page>
    );
}

export { Hero };