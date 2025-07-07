import {
    Avatar,
    AvatarFallback,
    AvatarImage,
} from "@/components/ui/avatar"

import { Button } from "@/components/ui/button";

import { User } from 'lucide-react';

function Header() {

    const username = import.meta.env.VITE_GH_USER;
    const project = import.meta.env.VITE_GH_PROJECT;

    return (
        <header className="flex w-full items-center justify-between">
            <div className="flex content-center gap-3">
                <div className="">
                    <Avatar>
                        <AvatarImage src={`https://github.com/${username}.png`} />
                        <AvatarFallback>
                            <User className="h-8 w-8" />
                        </AvatarFallback>
                    </Avatar>
                </div>
                <div className="flex items-center gap-2">
                    <a href={`https://github.com/${username}`}>
                        <Button variant="ghost">
                            <p className="text-md font-semibold">
                                {username}
                            </p>
                        </Button>
                    </a>

                    <div>
                        <p className="text-md font-semibold">/</p>
                    </div>

                    <a href={`https://github.com/${username}/${project}`}>
                        <Button variant="ghost">
                            <p className="text-md font-semibold text-muted-foreground ">
                                {project}
                            </p>
                        </Button>
                    </a>

                </div>

            </div>

        </header>
    );
}

export { Header };