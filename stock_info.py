import yfinance as yf
import pandas as pd

class Stock:
    def __init__(self, symbol):
        """
        주어진 주식 심볼(symbol)을 사용하여 Stock 객체를 초기화합니다.
        매개변수:
        symbol (str): 주식 심볼을 나타내는 문자열.
        """

        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    def get_basic_info(self):
        """
        주어진 주식 티커에 대한 기본 정보를 반환합니다.
        
        반환 형식:
            - 주식 티커의 기본 정보
        
        반환값:
            str: 기본 정보를 포함한 문자열
        """
        
        basic_info = pd.DataFrame.from_dict(self.ticker.info, orient='index', columns=['Value']) 
        return basic_info.loc[['longName', 'industry', 'sector', 'marketCap', 'sharesOutstanding']].to_markdown()
    

    def get_financial_statement(self):
        """
        주어진 주식 티커에 대한 분기별 재무제표를 반환합니다.
        
        반환 형식:
            - 분기별 손익계산서
            - 분기별 대차대조표
            - 분기별 현금흐름표
        
        반환값:
            str: 재무제표를 포함한 문자열
        """

        return f"""
        ### Quarterly Income Statement
        {self.ticker.quarterly_income_stmt.loc[['Total Revenue', 'Gross Profit', 'Operating Income', 'Net Income']].to_markdown()}

        ### Quarterly Balance Sheet
        {self.ticker.quarterly_balance_sheet.loc[['Total Assets', 'Total Liabilities Net Minority Interest', 'Stockholders Equity']].to_markdown()}

        ### Quarterly Cash Flow
        {self.ticker.quarterly_cash_flow.loc[['Operating Cash Flow', 'Investing Cash Flow', 'Financing Cash Flow']].to_markdown()}
        """

