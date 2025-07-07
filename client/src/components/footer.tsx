import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { User } from 'lucide-react';

import type { ReactNode } from "react";

type Link = {
    text: string;
    url: string;
    icon: ReactNode;
}

type FooterProps = {
    links: Link[];
}

function Footer({ links }: FooterProps) {
    return (
        <header className="flex w-full items-center justify-between">
            <div className="flex content-center gap-3">
                {
                    links.map((link, index) => {
                        return (
                            <div key={index} className="flex items-center gap-2">
                                <a href={link.url}>
                                    <Button variant="ghost">
                                        <span className="opacity-50">{link.icon}</span>
                                        <p className="text-md text-muted-foreground">
                                            {link.text}
                                        </p>
                                    </Button>
                                </a>
                            </div>
                        );
                    }
                    )
                }
            </div>
        </header>
    );
}

export { Footer };