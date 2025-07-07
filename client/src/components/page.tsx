type PageProps = {
    header: React.ReactNode;
    footer: React.ReactNode;
    children?: React.ReactNode;
}

function Page({ header, footer, children }: PageProps) {
    return (
        <div className="flex flex-col">
            <div className="border-b p-4">
                {header}
            </div>
            <div className="grow">
                <div className="flex flex-col items-center justify-center ">
                    {children}
                </div>
            </div>
            <div className="border-t p-4">
                {footer}
            </div>
        </div>
    );
}

export { Page };