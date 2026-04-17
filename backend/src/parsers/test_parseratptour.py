import asyncio

from parsers.atptour_parser import ATPTourParser


async def main():
    parser = ATPTourParser()
    result = await parser.parse("https://www.atptour.com/en/news/fonseca-rinderknech-munich-2026-wednesday")

    print("\nTITLE:")
    print(result["title"])

    print("\nDOMAIN:")
    print(result["domain"])

    print("\nHTML TEXT PREVIEW:")
    print(result["html_text"][:])

    print("\nPARSED TEXT PREVIEW:")
    print(result["parsed_text"][:])

    print("\nLUNGHEZZE:")
    print(f'html_text: {len(result["html_text"])} caratteri')
    print(f'parsed_text: {len(result["parsed_text"])} caratteri')


if __name__ == "__main__":
    asyncio.run(main())